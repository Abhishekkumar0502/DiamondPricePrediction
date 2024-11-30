from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='DiamondPricePrediction',  # Corrected brackets from {} to ()
    version='0.0.1',
    author='Abhishek Kumar',
    author_email='abhishek@gmail.com',
    install_requires=get_requirements('requirement.txt'),  # Fixed the typo in file name
    packages=find_packages()
)