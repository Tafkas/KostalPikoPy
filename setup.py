#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(name='pikopy',
      version='0.9.0',
      author='Christian Stade-Schuldt',
      author_email='stadeschuldt@gmail.com',
      url='https://github.com/Tafkas/KostalPikoPy',
      download_url='https://github.com/Tafkas/KostalPikoPy',
      description='A package for working with a Piko Inverter from Kostal',
      long_description='A package for working with a Piko Inverter from Kostal',

      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': ['*.txt', '*.rst'],
          'pikopy': ['data/*.html', 'data/*.css'],
      },
      exclude_package_data={'': ['README.txt']},

      #scripts=['bin/my_program'],

      keywords='python kostal piko inverter photovoltaic solar',
      license='GPL',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                   ],

      # setup_requires = ['python-stdeb', 'fakeroot', 'python-all'],
      install_requires=['setuptools'],
      )
