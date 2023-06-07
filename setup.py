from setuptools import find_packages,setup
from typing import List

requirements_file_name = "requirements.txt"
REMOVE_PAKAGE = "-e ."

def get_requirements()->List[str]:
    with open (requirements_file_name) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_name.replace("\n","")  for requirement_name in requirement_list]

    
    if REMOVE_PAKAGE in requirement_list:
        requirement_list.remove(REMOVE_PAKAGE)
    return requirement_list



setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industry Level Project',
      author='Lokesh Bisen',
      author_email='Lokesh.study11@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements()
    
     )

