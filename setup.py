#!/usr/bin/env python

from setuptools import setup

setup(
        name='GTKUtils',
        version='0.2.2',
        description='Various utilities for working with PyGTK.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: X11 Applications :: GTK',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
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
