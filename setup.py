#!/usr/bin/env python

import os
from setuptools import setup, find_packages
import re


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Get version without importing, which avoids dependency issues
def get_version():
    with open('geetools/_version.py') as version_file:
        return re.search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""",
                         version_file.read()).group('version')

# the setup
setup(
    name='geetools',
    version= get_version(),
    description='Set of tools to use in Google Earth Engine Python API',
    long_description=read('README.rst'),
    url='',
    author='Rodrigo E. Principe',
    author_email='fitoprincipe82@gmail.com',
    license='MIT',
    keywords='google earth engine raster image processing gis satelite',
    packages=find_packages(exclude=('docs', 'js')),
    include_package_data=True,
    install_requires=['requests', 'Pillow', 'ipyleaflet', 'folium', 'pyshp',
                      'pygal', 'pandas', 'ipywidgets', 'traitlets'],
    extras_require={
    'dev': [],
    'docs': [],
    'testing': [],
    },
    classifiers=['Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7'],
    )