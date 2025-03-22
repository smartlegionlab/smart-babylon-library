import os
import re
from setuptools import setup, find_packages


def get_version():
    init_path = os.path.join(os.path.dirname(__file__), "smart_babylon_library", "__init__.py")
    with open(init_path, "r", encoding="utf-8") as f:
        content = f.read()
    version_match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart_babylon_library",
    version=get_version(),
    author="A.A. Suvorov",
    author_email="smartlegiondev@gmail.com",
    description="A Python library for creating and manipulating text libraries, inspired by the Library of Babel concept and my own concept of Smart Passwords.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smartlegionlab/smart_babylon_library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
