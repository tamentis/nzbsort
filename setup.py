#!/usr/bin/python

from distutils.core import setup

from nzbsort import __version__

setup(
    name="nzbsort",
    version=__version__,
    description="NZB files alpha sorter",
    author="Bertrand Janin",
    author_email="tamentis@neopulsar.org",
    url="http://tamentis.com/projects/nzbsort/",
    scripts=["nzbsort.py"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Topic :: Communications :: Usenet News",
        "Topic :: Communications :: File Sharing",
    ]
)
