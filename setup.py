from marx import __version__
from setuptools import setup, find_packages
import os

README = "README.md"

base = os.path.dirname(__file__)
local = lambda x: os.path.join(base, x)

def read(fname):
    return open(local(fname)).read()

setup(
    name="marx-workflows",
    version=__version__,
    author="Nino Walker",
    author_email="nino.walker@gmail.com",
    description=read(README).split("\n", 1)[0],
    url='https://github.com/ninowalker/marx',
    license="BSD",
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=read(README),
    test_suite='nose.collector',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)


