from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT="-e ."
def get_requirements(filepath:str)->List[str]:
    '''
        THis function returns the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements ]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements





setup(
    name='MLproject',
    verison='0.0.1',
    author='Roshan',
    author_email='chowrasiar@alum.iisc.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)