#!/usr/bin/env Rscript
library("optparse")
library("MonoPhy")

option_list = list(
  make_option(c("-f", "--file"), type="character", default=NULL, 
              help="dataset file name", metavar="character", dest=file),
	make_option(c("-o", "--out"), type="character", default="out.tsv", 
              help="output file name [default= %default]", metavar="character", dest=out)
); 

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);


n <- length(opt$file)
for (i in 1:n){
  data <- read.tree(opt$file[i])
  tree_rooted <- midpoint(data)
  solution <- AssessMonophyly(tree_rooted)
  name_ext <- paste(opt$out, sep = "\t")
  write.csv(solution$Genera$result, file = name_ext)
}