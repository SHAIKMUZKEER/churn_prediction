from setuptools import setup , find_packages

from typing import List

HYPEN_E_DOT  = "-e ."

def get_requirments(file_path : str) -> List[str]:
    requirments = []
    with open(file_path , "r") as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments] 

        if HYPEN_E_DOT in requirments: 
            requirments.remove(HYPEN_E_DOT)

setup(
    name="churn_prediction",
    version="0.0.1",
    description="simple churn project prediction using the random forest classifer",
    author="muzkeer",
    author_email="muzkeer@example.com",
    packages = find_packages(), 
    install_requirments = get_requirments("requirments.txt")
)