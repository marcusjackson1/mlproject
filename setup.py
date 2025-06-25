from pathlib import Path
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Return a clean list of requirement strings.
    """
    with open(file_path, encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip()]

    # Drop editable-install directive if present
    if "-e ." in requirements:
        requirements.remove("-e .")

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Marcus Jackson",
    author_email="mjjackson@scu.edu",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
