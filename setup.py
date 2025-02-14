from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return a list of requirements.
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":  # Corrected condition
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst  # Ensure return in case of FileNotFoundError

print(get_requirements())

setup(
    
    name='my_package',
    author="sangam",
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
   

)