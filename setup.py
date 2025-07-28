from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements for the package.
    """
    requirement_lst: List[str] = []
    
    # Reading the requirements from the requirements.txt file
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
        for line in lines:
            requirement=line.strip()
            if requirement and requirement!='-e .':
                requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Deep Singh',
    author_email="deepsingh1312003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)