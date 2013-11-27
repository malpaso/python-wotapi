#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

# dep sugar.
_ver = sys.version_info

if _ver[0] == 2:
    dep = ['simplejson', 'requests']
elif _ver[0] == 3:
    dep = ['requests']

setup(
    name='wotapi',
    version='1.0',
    description='Unofficial WoT api wrapper for Python.',
    long_description=open('README.rst').read(),
    author='Bill Tindal',
    url='https://github.com/malpaso/python-wotapi',
    packages=find_packages(),
    download_url='',
    keywords='wotapi wot api wrapper worldoftanks',
    zip_safe=True,
    install_requires=dep,
    py_modules=['wotapi'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)