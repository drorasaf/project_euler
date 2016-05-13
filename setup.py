#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

name = 'Dror Asaf'
address = 'drorasaf87@gmail.com'

setup(name='euler',
      version='0.0.1',
      description="Solutions for project euler",
      author=name,
      author_email=address,
      url='https://github.com/drorasaf/project_euler',
      packages=find_packages(),
      license='Apache License, Version 2.0',
      keywords=['euler'],
      classifiers=[
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          ]
      )
