#!/usr/bin/env python

from setuptools import find_packages, setup
from xprobepy import __version__
from os import path
import sys

requirements = []

for flag, req in [('--with-pcap', 'pcap')]:
    if flag in sys.argv:
        sys.arg.remove(flag)
    else:
        requirements.append(req)

setup(
        name = 'xprobepy',
        version = __version__,
        description='Remote fingerprinting tool',
        author='Ofir Arkin, Yarochkin Fyodor, Meder Kydyraliev',
        author_email='xprobe@o0o.nu',
        url = 'http://xprobe.sourceforge.net',
        packages = find_packages(exclude=['tests']),
        install_requires=requirements,
        zip_safe=False,
        long_description=open(
            path.join(
                path.dirname(__file__),
                'README'
                )
            ).read(),
        test_suite = 'nose.collector',
        classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Topic :: Internet",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta"]
        
        )
