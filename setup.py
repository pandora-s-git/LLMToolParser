"""Python setup.py for LLMToolParser package"""
import io
import os
from setuptools import find_packages, setup

def read(*paths, **kwargs):
    """
    Read the contents of a text file safely.
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name = "LLMToolParser",
    version = "0.1.0",
    author = "pandora",
    description = "",
    url = "https://github.com/pandora-s-git/LLMToolParser",
    packages = find_packages(),
    install_requires = read_requirements("requirements.txt"),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)