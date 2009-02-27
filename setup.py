#!/usr/bin/env python

from setuptools import setup, find_packages
from glob import glob

setup(
        name='GTKUtils',
        version='0.1.3',
        description='Various small utilities for working with PyGTK.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: X11 Applications :: GTK',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Desktop Environment :: Gnome',
            'Topic :: Software Development :: User Interfaces',
            ],
        packages=[
            'gtkutils',
            ],
        )
