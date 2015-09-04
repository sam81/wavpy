#! /usr/bin/env python
# -*- coding: utf-8 -*-

from numpy.distutils.core import setup
from numpy.distutils.core import Extension

setup(name="wavpy",    
    version="0.2.6",
      py_modules=["wavpy"],
      author="Samuele Carcagno",
      author_email="sam.carcagno@gmail.com;",
      description="wavpy is a python module to read and write WAV files",
      long_description=\
      """
      Module for reading and writing WAV files. It is a simple but convenient wrapper to the scipy.io.wavfile module.
      """,
      license="GPL v3",
      url="",
      requires=['numpy (>=1.6.1)',
                'scipy (>=0.9)'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering'
          ]
      )
