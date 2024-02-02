from setuptools import find_packages ,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(filet_path:str)->List[str]:
    '''
    this function will return list of requiremnets
    '''
    requirements=[]
    with open(filet_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
   name='End to End ML Projects',
   versiob='0.0.1',
   auther='Rakesh Patel',
   auther_email='rockersinfo@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)