# command to run script
# Rscript --vanilla heatmap.R path/to/input path/to/output label title

#########################################################
### get arguments
#########################################################

args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if ( length(args) < 4) {
  print("Usage: Rscript --vanilla heatmap.R path/to/input path/to/output label title");
  stop("Usage: Rscript --vanilla heatmap.R path/to/input path/to/output label \nRscript --vanilla heatmap.R out_genes.txt out_genes.png 'Drug Classes' 'Read counts to drug classes using CARD's canonical'", call.=FALSE)
}

#########################################################
### load libraries
#########################################################

# install.packages('gplots', repos='http://cran.rstudio.com/')
library(gplots)
# install.packages('viridis', repos='http://cran.rstudio.com/')
library(viridis)
library(ggplot2)
# install.packages('dplyr', repos='http://cran.rstudio.com/')
library(dplyr)
# install.packages('tidyr', repos='http://cran.rstudio.com/')
library(tidyr)
# stat_binhex
# install.packages('hexbin', repos='http://cran.rstudio.com/')
library(reshape2)

#########################################################
### read data and transform it to matrix format
#########################################################

data <- read.csv(args[1], comment.char="#", sep="\t" , check.names = FALSE)
rnames <- data[,1]                       
mat_data <- data.matrix(data[,2:ncol(data)])
rownames(mat_data) <- rnames

#########################################################
### plotting heatmap
#########################################################

my_palette <- colorRampPalette(c("black", "#FFDB00", "#314ef9"))(n = 299)

cairo_ps(
  args[2],
  width = 10, 
  height = 10,
  bg = "transparent",
  pointsize = 12,
  onefile = FALSE,
  fallback_resolution = 300
)

row_distance = dist(mat_data, method = "manhattan")
row_cluster = hclust(row_distance, method = "ward.D2")
col_distance = dist(t(mat_data), method = "manhattan")
col_cluster = hclust(col_distance, method = "ward.D2")

melted_cormat <- melt(t(mat_data))

gg <- ggplot(melted_cormat, aes(x=Var2, y=Var1, fill=value))
gg <- gg + geom_tile(color="black", size=0.25)
gg <- gg + coord_equal() + ggtitle(label=args[4]) 
gg <- gg + theme(panel.grid.major = element_blank(), axis.text.x=element_text(angle = 90, hjust = 0, vjust = 0.5), rect = element_rect(fill = "transparent")) 
gg <- gg + scale_fill_gradientn(name="Read counts", colors = my_palette, limits=range(melted_cormat$value, 12000), na.value = "#FDE725FF")
gg <- gg + xlab("Isolates") + ylab(args[3])
gg

dev.off()
