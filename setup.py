#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='PyPhisher',
    version=version,
    description='Ferramenta de phishing definitiva em python com tunelamento duplo, 77 modelos e muito mais!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='BlackTrace',
    author_email='blacktracee@gmail.com',
    license="MIT",
    url='https://github.com/BlackTracee',
    scripts=['pyphisher'],
    install_requires=["requests", "bs4", "rich"]
)
