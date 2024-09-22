from setuptools import find_packages, setup
from typing import List

HEd = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [x.replace("\n", "") for x in requirements]

        if HEd in requirements:
            requirements.remove(HEd)

setup(
    name='mlproject',
    version='0.0.1',
    author='Tarsem',
    author_email='tarsemj7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
