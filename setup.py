#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="NAuRA",
    version="1.0",
    author="Arnaud Felten, Déborah Merda",
    author_email="arnaud.felten@anses.fr, deborah.merda@anses.fr",
    description="Nice Automatic Research of Alleles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afelten-Anses/NAuRA",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: Linux",
    ],
        scripts=['NAuRA',
             "NAuRA_BPF",
             ],
    include_package_data=True,
    install_requires=['biopython>=1.68'
                      ],
    zip_safe=False,

)
