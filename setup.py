from setuptools import setup, find_packages
import os

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

libFolder = os.path.dirname(os.path.realpath(__file__))
reqsFile = libFolder + "/reqs.txt"

if os.path.isfile(reqsFile):
    with open(reqsFile) as f:
        install_requires = f.read().splitlines()

setup(
    name="tuser",
    version="0.1.6",
    author="Daniil Baikalov",
    author_email="felix.trof@gmail.com",
    description="Tuser allows you to create databases for users of your project.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="GNU",
    classifiers=classifiers,
    url="",
    packages=find_packages(),
    install_requires=[
        "requests",
        "prettytable"
    ],
    entry_points= {
        "console_scripts" : ['tuser = Tuser.tuser:main']
    }
)
