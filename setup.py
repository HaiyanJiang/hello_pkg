#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:41:58 2020

@author: ginger
@email:  gingerxjiang@gmail.com
"""

# from distutils.core import setup
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hellopkg",
    version="0.0.1",
    author="ginger",
    author_email="gingerxjiang@gmail.com",
    description="A hello package to install module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        ],
    # packages=setuptools.find_packages(),
    py_modules=[
        "hellopkg.add_method",
        "hellopkg.gendata.gen_random",
        "hellopkg.gendata.hello_gen",
        "hellopkg.utils.functions",
        ]
    )

