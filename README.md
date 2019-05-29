# asm_microbe_2019_rgi
This repository is for RGI - ASM Microbe 2019 poster 

### Abstract Title:

Resistance Gene Identifier (RGI) - Prediction of antimicrobial resistance genes and mutations for genomic and metagenomic sequencing data

### Author(s) Information: 

Amogelang R. Raphenya, Tammy T. Y. Lau, Brian Alcock, Kara K. Tsang, Finlay Maguire, F.S. Brinkman, R.G. Beiko, & Andrew G. McArthur

### Abstract:

Antimicrobial resistance (AMR) is a major health crisis and a global concern. Increased global travel is compounding the problem, as resistance is spread from one region to another. As an evolutionary process spanning the clinic, farm, and environment, bacteria are
capable of developing new resistance mechanisms. Improved sequencing technology offers a solution, but to use it we need the Comprehensive Antibiotic Resistance Database (CARD; card.mcmaster.ca) and Resistance Gene Identifier software (RGI; card.mcmaster.ca/analyze/rgi or github.com/arpcard/rgi). Sequence analysis tools need robustly curated databases such as CARD for resistome prediction. CARD is both an ontology- and a detection model-centric database. Reference data curation based on sequence detection models allows CARD to be easily expanded as new AMR determinants are discovered. For each AMR determinant, CARD provides three classifications: i.e., drug class, AMR gene family, and resistance mechanism. We developed RGI to predict AMR determinants from genomes and metagenomic datasets. RGI uses four sequence detection models: protein homolog, protein variant, rRNA gene variant, and protein overexpression. RGI can be used to analyze complete genome sequences, draft genome or metagenome assemblies, and raw genome or metagenome reads. For genome sequences and assemblies, RGI uses a combination of gene prediction, BLAST against CARD, and mutation mapping to predict resistance determinants, providing results in a unique paradigm of Perfect, Strict, and Loose hits. Perfect hits mean the predicted AMR determinant matches a known reference sequence in CARD and Strict hits pass manually curated bit-scores curated for each detection model. Strict hits are likely functional variants. Loose hits fall below the bit-score cutoff. Loose hits are likely distant homologs or new emergent threats. RGI for metagenomics uses the Burrows-Wheeler Transform (through BWA or Bowtie2 software) to align reads to CARD reference sequences and in silico predicted allelic variants from CARD’s Resistomes & Variants data set (card.mcmaster.ca/genomes), the latter which we illustrate is critical for complete resistome prediction. In addition, RGI uses AMR specific k-mers mined from CARD Resistomes & Variants to predict pathogen-of-origin for detected AMR alleles and mobile AMR genes. Lastly, RGI includes additional algorithms to support analysis of AMR in metagenomic samples via bait capture technologies by helping with probe design and validation.

### Methods:

#### RGI for genenomes:

RGI analyzes genomes under three paradigms: Perfect, Strict, and Loose. The Perfect hits matches to the curated reference sequences in CARD. The Strict algorithm detects previously unknown variants of known AMR genes, including secondary screen for mutations, using detection models with CARD's curated bitscore cut-offs. The Loose falls below the detection model cut-offs and provides detection of new, emergent threats of AMR genes.

#### RGI for metagenomes:



### Results:

#### RGI for genenomes:

#### RGI for metagenomes:

### Future directions:

- Add perfect, strict and loose paradigm for RGI metagenomics
- AMR Single nucleotide polymorphism (SNPs) screening
- Distinguish between AMR genes for gram positive and gram negatives bacteria

### Acknowledgements:

I would like to thank Allison Guitor, Bhavya Singh and McArthur lab for their continued support.

### References:

Jia, B., et al. CARD 2017: expansion and model-centric curation of the Comprehensive Antibiotic Resistance Database. 
Nucleic Acids Research, 45, D566-573.

Hendriksen, R.S., et al. Global monitoring of antimicrobial resistance based on metagenomics analyses of urban sewage. 
Nature Communications, 2019 vol.10(1) p.1124

