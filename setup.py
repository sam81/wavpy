[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"


[project]
name = "wavpy"
    version="0.3.1",
authors = [
  { name="Samuele Carcagno", email="sam.carcagno@gmail.com" },
]
description = "wavpy is a python module to read and write WAV files"
readme = "README.md"
requires-python = ">=3.7"
dependencies = ["numpy (>=1.0.0)",
                "scipy (>=1.0.1)"]

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Topic :: Scientific/Engineering"
]

[project.urls]
"Homepage" = "https://github.com/sam81/wavpy"
"Bug Tracker" = "https://github.com/sam81/wavpy/issues"

[tool.hatch.build]
include = [
  "wavpy.py",
  "tests/*.py",
  "test_wavs/*.wav",
  "doc/*
]

exclude = [
  "old_other/*"
]