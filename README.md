NAuRA README
================

Authors: Arnaud Felten, Déborah Merda

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)

You can find the latest version of the tool at [https://github.com/afelten-Anses/NAuRA](https://github.com/afelten-Anses/NAuRA)

HTML and PDF technical documentation are available in the 'docs/' directory.


NAuRA workflow
==================

This workflow called NAuRA for "Nice automated research of variants" aims to ... 

The differents workflow steps and scripts are presented below :

![](workflow.jpg?raw=true "NAuRA workflow")



Quick Start
===========

## Usage (Linux/Mac OS X)

If it's necessary, make NAuRA excecutable :

	chmod +x NAuRA

Add the scripts to your bashrc or bash_profile :

	export PATH=$PATH:NAuRA/
	
Then you can run it as shell command :

	NAuRA


Dependencies
============

NAuRA has been developped with python 2.7 (tested with 2.7.12).


## External dependencies

* [Biopython](http://biopython.org/wiki/Download) tested with 1.70
* [blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) - tested with 2.2.31+
* [Fastx-toolkit](http://hannonlab.cshl.edu/fastx_toolkit/download.html) - tested with 0.0.14
* [pairdist](https://github.com/frederic-mahe/pairdist) - tested with 1.0	
* [clustalo](http://www.clustal.org) - tested with 2.1
* [Dendropy (sumtrees.py)](https://pythonhosted.org/DendroPy/programs/sumtrees.html) - tested with 4.3.0


Parameters
==========

Parameters of each scripts are available with one of its 3 options :

	NAuRA
	NAuRA -h
	NAuRA --help

## NAuRA parameters

* -i : Folder with GBK files, theses files must be in the format 'GENOMEid.gbk' (REQUIRED)
* -m : Matrix file if exists (default:matrix.tsv)
* -q : Text file with query Fasta path, one per line (REQUIRED). Optional, set cov and id percent separated by tabulation. Add '_1' for each query. No supplementary '_' character. Each query file name must have the same name as the allele name.")
* -l : Text file with the already analyzed genomes list (default:list.txt)
* -pl : Minimum percent of alignment coverage (default:80)
* -ph : Minimum percent of alignment identity (default:80)
* -T : Number of threads to use (default:2)
* -b : Number of bootstrap, only with --withPhylo option (default:1)

## NAuRA options

* --nucl : Specify query are nucleic sequences
* --withPhylo : Do the phylogeny analysis of new alleles
* --keepBlastAln : Keep blast results for each genome
* --noDrift : Similarity and coverage always tested with default allele (take longer, recommended if queries sequences are close)

## Queries file

NAuRA need a queries file where is specified the path of all queries fasta files. Queries must be in a separated fasta file and the query header must end with "_1" (see example below). This allows NAuRA to detect the intial query and to increment the allele number.

	>queryA_1
	SIPFNANWLNQQYAEIIQAILFDVVGYEVKPHFITTEELANYSNNETATPKETTKPST
	ETTEDNHVLGREQFNAHNTFDTFVIGPGNRFPHAASLAVAEAPAKAYNPLFIYGGVGL
	GKTHLMHAIGHHVLDNNPDAKVIYTSSEKFTNEFIKSIRDNEGEAFRERYRNIDVLLI

	
Optionally, a specific minimum of coverage (column 1) and minimum of identity (column 2) can be setting for each query. If no value are is specified, values given by '-pl' and '-ph' arguments are setting by default. Values must be separated by a tab character.

	/data/myProject/queryA.fasta
	/data/myProject/queryB.fasta	90	90
	/data/myProject/queryC.fasta	95	
	/data/myProject/queryD.fasta		70


Ouputs
======


--> important : ne pas mélanger prot et nucl
--> exemple entrée query tsv
--> exemple fasta query avec nouveau allèle
--> exemple matrice


