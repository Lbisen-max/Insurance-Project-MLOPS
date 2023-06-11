

# Missing value input
# Outliars handling
# Imbalanced data handling
# Convert categorical data into numerical data


from Insurance.entity import config_entity,artifact_entity
from Insurance.exceptions import InsuranceException
from Insurance.logger import logging
from typing import Optional
import sys
import os
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from Insurance.config import TARGET_COLUMN
from sklearn.preprocessing import LabelEncoder
from Insurance import utils
#from sklearn.combine import SMOTE


class DataTransformation:

    def __init__ (self,data_transformation_config:config_entity.DataTransformationConfig,
                  data_ingestion_artifact:artifact_entity.DataIngestionArtifact):

        
        try:
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e,sys)

        
    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            simple_imputer= SimpleImputer(strategy="constant",fill_value=0)
            robust_scaler = RobustScaler()
            pipeline= Pipeline(steps=[
                    ('Imputer',simple_imputer),
                    ('Robust_scaler',robust_scaler)
                ])

            return pipeline
                         
        except Exception as e:
                raise InsuranceException(e,sys)
            
                            

    def initiate_data_transformation(self,)->artifact_entity.DataTransformationArtifact:
        try:
            logging.info("reading dataset")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            input_features_train_df = train_df.drop(TARGET_COLUMN,axis=1)
            input_features_test_df = test_df.drop(TARGET_COLUMN,axis=1)

            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            label_encoder = LabelEncoder()

            # fit data
            logging.info("fitting train and test data")
            target_feature_train_arr = target_feature_train_df.squeeze()
            target_feature_test_arr = target_feature_test_df.squeeze()


            for col in input_features_train_df.columns:
                if input_features_test_df[col].dtypes == 'O':
                    input_features_train_df[col] = label_encoder.fit_transform(input_features_train_df[col])
                    input_features_test_df[col] = label_encoder.fit_transform(input_features_test_df[col])

                else:
                    input_features_train_df[col] = input_features_train_df[col]
                    input_features_test_df[col] = input_features_test_df[col]
            logging.info("initializing the pipeline")
            
            transformation_pipeline = DataTransformation.get_data_transformer_object()
            transformation_pipeline.fit(input_features_train_df)

            input_feature_train_arr = transformation_pipeline.transform(input_features_train_df)
            input_feature_test_arr = transformation_pipeline.transform(input_features_test_df)
            logging.info("concatinating the features and target array")
            train_arr = np.c_[input_feature_train_arr,target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr,target_feature_test_arr]

            logging.info("saving the object")

            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_train_path,
            array=train_arr)

            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_path,
            array=test_arr)

            utils.save_object(file_path=self.data_transformation_config.transform_object_path,obj=transformation_pipeline)


            utils.save_object(file_path=self.data_transformation_config.target_encoder_path,obj=label_encoder)

            data_transformation_artifact = artifact_entity.DataTransformationArtifact(
                transform_object_path=self.data_transformation_config.transform_object_path,
                transformed_train_path = self.data_transformation_config.transformed_train_path,
                transformed_test_path = self.data_transformation_config.transformed_test_path,
                target_encoder_path = self.data_transformation_config.target_encoder_path
            )


            return data_transformation_artifact
    

         
        except Exception as e:
            raise InsuranceException(e,sys)

            