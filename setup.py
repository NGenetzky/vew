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
    entry_points={
        'console_scripts': [
            'vew = vew.__main__:main',
            'vew_hugo = vew.hugo.__main__:main',
        ],
        # 'virtualenvwrapper.get_env_details': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.initialize': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.postactivate': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.postdeactivate': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.postmkproject': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.postmkvirtualenv': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.postrmvirtualenv': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.preactivate': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.predeactivate': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.premkproject': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.premkvirtualenv': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.prermvirtualenv': ['vew = vew.__main__:stub'],
        # 'virtualenvwrapper.pre_activate': ['vew = vew.__main__:stub'],
    },
    include_package_data=True,

    data_files=[
        ( 'share/vew/hugo_config', [
            'data/hugo_config/config.toml',
            'data/hugo_config/menus.toml',
            'data/hugo_config/params.toml',
        ]),
    ]
)
