# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup

setup(name='MySQLreplica',
      version='0.1',
      description='Monitor MySQL replica',
      url='https://github.com/mohtork/mysql-replication-monitor',
      author='Torkey',
      author_email='',
      setup_requires='setuptools',
      package_dir={'': 'replica-monitor'},
      packages=find_packages(where='replica-monitor'),
      license='Apache 2.0',
      zip_safe=False)
