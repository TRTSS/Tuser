from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

setup(
    name="Ziplit.Tuser",
    version="0.1.0",
    author="Daniil Baikalov",
    author_email="felix.trof@gmail.com",
    description="Tuser allows you to create databases for users of your project.",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    license="GNU",
    classifiers=classifiers,
    url="",
    packages=find_packages(),
)
