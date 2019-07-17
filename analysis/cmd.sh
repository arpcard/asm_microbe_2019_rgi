### create heatmap data for card cannonical using create_heatmap_data.py script
python3 create_heatmap_data.py -i datasets_card/

mv out_drug_class.txt out_drug_class_cannonical.txt
mv out_resistance_mechanism.txt out_resistance_mechanism_cannonical.txt
mv out_genes.txt out_genes_cannonical.txt

### plot heatmap for card cannonical - drug classes vs isolates
Rscript --vanilla heatmap.R out_drug_class_cannonical.txt out_drug_class_cannonical.eps 'Drug Classes' "Read counts to drug classes using CARD's canonical"

### plot heatmap for card cannonical - resistance mechanism vs isolates
Rscript --vanilla heatmap.R out_resistance_mechanism_cannonical.txt out_resistance_mechanism_cannonical.eps 'Resistance Mechanism' "Read counts to drug classes using CARD's canonical"

### plot heatmap for card cannonical - genes vs isolates
Rscript --vanilla heatmap.R out_genes_cannonical.txt out_genes_cannonical.eps 'Genes' "Read counts to drug classes using CARD's canonical"

### create heatmap data for card variants / wild using create_heatmap_data.py script
python3 create_heatmap_data.py -i datasets_wild/

mv out_drug_class.txt out_drug_class_variants.txt
mv out_resistance_mechanism.txt out_resistance_mechanism_variants.txt
mv out_genes.txt out_genes_variants.txt

### plot heatmap for card cannonical & variants - drug classes vs isolates
Rscript --vanilla heatmap.R out_drug_class_variants.txt out_drug_class_variants.eps 'Drug Classes' "Read counts to drug classes using CARD's canonical & full length in silico variants"

### plot heatmap for card cannonical & variants - resistance mechanism vs isolates
Rscript --vanilla heatmap.R out_resistance_mechanism_variants.txt out_resistance_mechanism_variants.eps 'Resistance Mechanism' "Read counts to drug classes using CARD's canonical & full length in silico variants"

### plot heatmap for card cannonical & variants - genes vs isolates
Rscript --vanilla heatmap.R out_genes_variants.txt out_genes_variants.eps 'Genes' "Read counts to drug classes using CARD's canonical & full length in silico variants"

### cleanup remove temp files (comment this out for debugging)
rm out_*.txt