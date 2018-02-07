NAuRA README
================

Authors: Arnaud Felten, Déborah Merda

Affiliation: [Food Safety Laboratory – ANSES Maisons Alfort (France)](https://www.anses.fr/en/content/laboratory-food-safety-maisons-alfort-and-boulogne-sur-mer)

You can find the latest version of the tool at [https://github.com/afelten-Anses/NAuRA](https://github.com/afelten-Anses/NAuRA)

HTML and PDF technical documentation are available in the 'docs/' directory.


NAuRA workflow
==================

This workflow called iVARCall2 for "independant variant calling 2" aims to perform the variant calling analysis from Illumina paired-end reads based on the GATK HaplotypeCaller algorithm. Each sample are processing independently and a g.vcf file is produce for each of them. This allow to combin several iVARCall2 results if the same reference genome is used. 

The differents workflow steps and scripts are presented below :

![](workflow.jpg?raw=true "NAuRA workflow")

- A driving script called 'iVARCall2' invokes 'BAMmaker', 'iVCFmaker', 'iVCFmerge', 'iVCFilter', 'VCFtoMATRIX', 'VCFtoFASTA', VCFtoPseudoGenome' and 'iReportMaker2' successively. 

- The script 'BAMmaker' allows trimming of paired-end reads with Trimmomatic, read alignment against a reference genome with BWA, read sorting with Samtools, and potentially duplication removal and realignment around InDels with the Genome Analysis Toolkit (GATK), successively.  

- Following an approved framework for variant discovery, the scripts 'iVCFmaker' call and filter variants (i.e. SNPs and InDels) according to GATK best practices in order to retain high-confidence variants and make a g.vcf file for each sample.

- The script 'iVCFmerge' merge all g.vcf in a single vcf file.

- All variants detected are filered by 'VCFilter' in order to remove variants caused by missing data or due to reference.

- The script 'VCFtoMATRIX' make 3 distance matrix (SNPs, InDels and SNPs + InDels) from all variants selected by the workflow.

- All filered variants are concatenante in a 3 fasta files (SNPs, InDels and SNPs + InDels) by the 'VCFtoFASTA' script. This fasta files can be used to produce a phylogenetic tree.

- The 'VCFtoPseudoGenome' script replace for each sample all SNPs in the reference genome in order to obtain a 'PseudoGenome'. For this step, InDels are not included.

- Finaly, the script "iReportMaker2" produce a pdf file where several variant calling informations and parameters are listed. 

Each script can also be invoked independently.


Quick Start
===========

## Usage (Linux/Mac OS X)

If it's necessary, make all scripts excecutable :

	chmod +x src/*

Add the scripts to your bashrc (/home/username/.bashrc) :

	export PATH=$PATH:NAuRA/
	
Then you can run it as shell command :

	NAuRA


Dependencies
============

NAuRA has been developped with python 2.7 (tested with 2.7.12).

## Important

This workflow needs 'BAMmaker', 'VCFtoMATRIX', 'VCFtoFASTA' and 'VCFtoPseudoGenome' scripts in your $PATH. This scripts are available in the VARCall/src directory of the VARtools git repository.


## External dependencies

* [blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) - tested with 2.2.31+
* [Fastx-toolkit](http://hannonlab.cshl.edu/fastx_toolkit/download.html) - tested with 0.0.14
* [pairdist](https://github.com/frederic-mahe/pairdist) - tested with 1.0	
* [clustalo](http://www.clustal.org) - tested with 2.1
* [Dendropy (sumtrees.py)](https://pythonhosted.org/DendroPy/programs/sumtrees.html) - tested with 4.3.0


Parameters
==========

Parameters of each scripts are available with one of its 3 options (example for iVCFmaker):

	iVCFmaker
	iVCFmaker -h
	iVCFmaker --help

## iVARCall2 parameters

* -a : adaptaters FASTA file (REQUIRED)
* -TRIMJAR : Trimmomatic jar path
* -GATKJAR : GenomeAnalysisTK jar path
* -PICARDJAR : picard-tools jar path
* -o : output prefix (default:output)
* -q : minimum phred score per base for trimming (default:30)
* -l : minimum read length for trimming (default:50)
* -PL : sequencing plateform for RG line (default:UNKNOWN)
* -PU : sequencer ID for RG line (default:UNKNOWN)
* -LB : sequencing library (default:UNKNOWN)
* -T : maximum number of threads to use (default:1)
* -m : maximum memory to use in Mb (default:4000)

## iVARCall2 options

* --removeDuplicates : remove duplicates reads (recommended)
* --indelRealigner : local realignment around indels (recommended)
* --removeTmpFiles : remove temporary files (recommended)
* --onlyVCF : stop process after making independent g.vcf files


Ouputs
======





