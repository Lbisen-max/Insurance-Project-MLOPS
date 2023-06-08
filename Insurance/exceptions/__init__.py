import os
import sys


# defining the class object for exception
class InsuranceException(Exception):

#defiing the function and supper class
    def __init__(self,error_message: Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message,error_details=error_details)


    @staticmethod
    def error_message_detail(error: Exception,error_details:sys)->str:
        _,_, exc_tb = error_details.exc_info()
        line_number = exc_tb.tb_frame.f_lineno
          
        # extracting file name from exception trackback
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Preparing error message
        error_message = f"Error occuread python script name [{file_name}]" \
                        f"line number [{exc_tb.tb_lineno}] error message [{error}]."
        

        return error_message
    
    def __str__(self):
        return InsuranceException.__name__.__str__()
    






