from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup  # Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

setup(
    name="covid_cajamar",
    version="0.0.1",
    description="Data gathering and visualization for covid data from Cajamar city.",
    author="Alexandre Farias",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)