#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

# Handle encoding
if sys.version_info[0] >= 3:
    def rd(filename):
        f = open(filename, encoding="utf-8")
        r = f.read()
        f.close()
        return r
else:
    def rd(filename):
        f = open(filename)
        r = f.read()
        f.close()
        return r

vre = re.compile("__version__ = \"(.*?)\"")
m = rd(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mviz", "__init__.py"))
version = vre.findall(m)[0]


setup(
    name="mviz",
    version=version,
    author="Alexander Mendez",
    author_email="bluespace@gmail.com",
    packages=["mviz"],
    url="http://github.com/ajmendez/mviz",
    license="MIT",
    description="Mendez Visualization Package",
    long_description=rd("README.md"),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)