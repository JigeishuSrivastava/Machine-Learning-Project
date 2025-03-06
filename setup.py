from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requiremenets= file_obj.readlines()
        requiremenets=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requiremenets:
            requiremenets.remove(HYPEN_E_DOT)

    return requiremenets



setup(
name= 'mlproject',
version='0.0.1',
author='Jigeishu Srivastava',
author_email='srivastavajigeishu933@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')





)