#!/usr/bin/env python

from setuptools import setup

setup(name='tap-facebook',
      description='Singer.io tap for extracting data from the Facebook Ads API',
      author='Stitch',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_facebook'],
      install_requires=[
          'attrs==22.2.0',
          'backoff==2.2.1',
          'pendulum==2.1.2',
          'facebook_business==16.0.0',
          'requests==2.28.2',
          'singer-python==5.13.0',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipdb',
              'nose',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-facebook=tap_facebook:main
      ''',
      packages=['tap_facebook'],
      package_data = {
          'tap_facebook/schemas': [
              # add schema.json filenames here
          ],
          'tap_facebook/schemas/shared': [
          ]
      },
      include_package_data=True,
)
