#!/usr/bin/env python2

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NAuRA",
    version="0.1",
    author="Arnaud Felten",
    author_email="arnaud.felten@anses.fr",
    description="NAuRA: Nice automated research of alleles ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afelten-Anses/NAuRA",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2",
        "Operating System :: POSIX :: Linux",
    ],
        scripts=["NAuRA",
             "NAuRA_BPF",
             "extract_alleles_from_blast",
             "pairdist.py"
             ],
    include_package_data=True,
    install_requires=['fastx_toolkit',   
                      'blast',
                      'biopython',
                      'clustalo',
                      'clustalw',
                      'dendropy',
                      'phylip',
                      ], 
    dependency_links=['https://github.com/frederic-mahe/pairdist'], 
    zip_safe=False,

)
