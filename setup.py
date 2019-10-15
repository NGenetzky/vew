#!/usr/bin/env python

from setuptools import setup, find_packages


PROJECT = 'vew'
VERSION = '0.0.1'

DESCRIPTION = ('Package designed for use with virtualenvwrapper')
try:
    LONG_DESCRIPTION = open('README.md', 'rt').read()
except IOError:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name=PROJECT,
    version=VERSION,

    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,

    author='Nathan Genetzky',
    author_email='nathan@genetzky.us',

    url='https://github.com/ngenetzky/vew',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    platforms=['Any'],
    # provides=['virtualenvwrapper.vew'], # TODO
    requires=[
        'virtualenv',
        'virtualenvwrapper (>=4.0)',
    ],
    # namespace_packages=['virtualenvwrapper'], # TODO
    packages=find_packages(),
    # entry_points={ # TODO
    #     'virtualenvwrapper.project.template': [
    #         'vew = virtualenvwrapper.vew:template',
    #     ],
    # },
    # include_package_data=True,
)
