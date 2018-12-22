#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='freesmsapi',
      version='0.1a',
      description='Envoyez vous des notifications avec l\'API SMS de Free',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat',
      ],
      keywords='free mobile, sms, api',
      url='https://github.com/chalios/freesmsapi',
      author='chalios',
      author_email='chalios@protonmail.com',
      license='MIT',
      packages=['freesmsapi'],
      install_requires=['requests'],
      include_package_data=True,
      zip_safe=False)
