from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''   
    this function will return the list of requirements from the file path
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        # requirements=file_obj.read().splitlines()
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
  
setup(
    name='mlpoject',
    version='0.0.1',
    author='skongonda',
    author_email='skongonda@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)