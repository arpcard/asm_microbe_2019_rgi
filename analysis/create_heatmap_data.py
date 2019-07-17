import csv, os, sys, argparse, glob

# read all tsv files and create csv as shown:

# Drug classes = 25
# 			,drug_class_1,		drug_class_2,		drug_class_3,	drug_class_4
# isolate_1,	0.094,				0.668,				0.4153,			0.4613
# isolate_2,	0.1138,				-0.3847,			0.2671,			0.1529


# AMR Gene Family = 24
# 			,amr_gene_family_1,		amr_gene_family_2,		amr_gene_family_3,	amr_gene_family_4
# isolate_1,	0.094,				0.668,				0.4153,			0.4613
# isolate_2,	0.1138,				-0.3847,			0.2671,			0.1529


# Resistance Mechanism = 26
# 			,resistance_mechanism_1,		resistance_mechanism_2,		resistance_mechanism_3,	resistance_mechanism_4
# isolate_1,	0.094,				0.668,				0.4153,			0.4613
# isolate_2,	0.1138,				-0.3847,			0.2671,			0.1529
delimiter="\t"

def get_headers(files, category):
	headers = [""]
	for f in files:
	    with open(f, 'r') as fp:
	        i = csv.reader(fp, delimiter='\t')
	        o_f_path, o_f_name = os.path.split(os.path.abspath(f))
	        filename = o_f_name.split(".gene_mapping_data.txt")[0]
	        for line in i:
	        	if "ARO Term" not in line:
	        		# print(line[category])
	        		items = line[category].split("; ")
	        		for i in items:
	        			if i.strip() not in headers:
	        				headers.append(i.strip())
	# print(headers)
	# print("--------")
	# print(headers)
	headers.sort()
	# print(headers)
	# exit("?")
	return headers

def get_isolates_alt(files, category, average_percent_coverage, filter_by=""):
	isolates = {}
	for f in files:
	    with open(f, 'r') as fp:
	        i = csv.reader(fp, delimiter='\t')
	        o_f_path, o_f_name = os.path.split(os.path.abspath(f))
	        filename = o_f_name.split(".gene_mapping_data.txt")[0]
	        # print(filename)
	        if "_wild" in filename:
	        	filename_dict = filename.split("_")
	        	filename = filename_dict[0]
	        # print(filename)
	        for line in i:
	        	if "ARO Term" not in line:
	        		items = line[category].split("; ")
	        		
	        		# filter by specific genes
	        		if filter_by in line[0]:
	        			items = line[category].split("; ")
	        		elif filter_by != "":
	        			items = []
	        		# print(items)
	        		for c in items:
	        			# if "sul" in line[0]:
	        				# print(c, " , ", line[0], line[average_percent_coverage])
	        			# print(">>>>>", c, ": ", line[average_percent_coverage], line[0])
	        			if filename not in isolates.keys():
	        				# print("1", c)
	        				isolates[filename] = {c: [line[average_percent_coverage]]}
	        				# if line[average_percent_coverage] == "100.00":
	        				# 	isolates[filename] = {c: line[average_percent_coverage]}
	        				# else:
	        				# 	isolates[filename] = {c: 0}

	        			else:
	        				# print("2", c, " => ", isolates[filename].keys())
	        				if c not in isolates[filename].keys():
	        					isolates[filename].update({c: [line[average_percent_coverage]]})
	        				else:
	        					isolates[filename][c].append(line[average_percent_coverage])
	        				# if line[average_percent_coverage] == "100.00":
	        				# 	isolates[filename][c] = line[average_percent_coverage]
	        				# else:
	        				# 	isolates[filename][c] = 0
	# average
	# from scipy import mean
	# isolates_ave = {}
	for i in isolates:
		for c in isolates[i]:
			# temp = isolates[i][c]
			# print(c, "=>", isolates[i][c])
			# isolates[i][c] = format(sum(map(float, isolates[i][c]))/ len(isolates[i][c]), ".2f")
			isolates[i][c] = format(sum(map(float, isolates[i][c])), ".2f")
	# sort
	isolates = dict(sorted(isolates.items()))
	import collections
	isolates = collections.OrderedDict(sorted(isolates.items()))
	return isolates

def get_isolates(files, category, average_percent_coverage, filter_by=""):
	isolates = {}
	for f in files:
	    with open(f, 'r') as fp:
	        i = csv.reader(fp, delimiter='\t')
	        o_f_path, o_f_name = os.path.split(os.path.abspath(f))
	        filename = o_f_name.split(".gene_mapping_data.txt")[0]
	        for line in i:
	        	if "ARO Term" not in line:
	        		items = line[category].split(";")
	        		# filter by specific genes
	        		if filter_by in line[0]:
	        			items = line[category].split(";")
	        		elif filter_by != "":
	        			items = []

	        		for c in items:
	        			if filename not in isolates.keys():
	        				isolates[filename] = {c: line[average_percent_coverage]}
	        				# if line[average_percent_coverage] == "100.00":
	        				# 	isolates[filename] = {c: line[average_percent_coverage]}
	        				# else:
	        				# 	isolates[filename] = {c: 0}

	        			else:
	        				isolates[filename][c] = line[average_percent_coverage]
	        				# if line[average_percent_coverage] == "100.00":
	        				# 	isolates[filename][c] = line[average_percent_coverage]
	        				# else:
	        				# 	isolates[filename][c] = 0

	return isolates

def write_csv(output_filename, headers, isolates, accessions_to_country):
	# print(accessions_to_country)
	# new = {}
	# # replace name in isolates
	# for i in isolates:
	# 	if "_wild" in i:
	# 		t = i.split("_wild")
	# 		# print(t)
	# 		new_name = "{}_wild".format(accessions_to_country[t[0]])
	# 		isolates[i] = {new_name: isolates[i]}
	# 		new.update({new_name:isolates[i]})
	# # sort
	# import collections
	# new = collections.OrderedDict(sorted(new.items()))
	# isolates = new
	with open(output_filename, 'w') as fp:
		writer = csv.writer(fp, delimiter=delimiter, dialect='excel')
		writer.writerow(headers)
		for i in isolates:
			row = []
			# if "_wild" in i:
			# 	t = i.split("_wild")
			# 	row.append("{}_wild".format(accessions_to_country[t[0]]))
			# else:
			# 	row.append(accessions_to_country[i])
			row.append(i)
			for h in headers:
				if h not in [""]:
					if h in isolates[i].keys():
						row.append(isolates[i][h])
					else:
						row.append(0)
			writer.writerow(row)

def trim_headers(input_file,output_file="test.txt"):
	rows = []
	headers = []
	with open(input_file, 'r') as fp:
		reader=csv.reader(fp, delimiter=delimiter)
		for row in reader:
			if "" == row[0]:
				# print(row)
				for h in row:
					if h.endswith(" beta-lactamase"):
						headers.append(h[:-15].strip())
					elif h.endswith(" antibiotic"):
						headers.append(h[:-11].strip())
					else:
						headers.append(h.strip())
			else:
				rows.append(row)
	# write new file
	with open(output_file, 'w') as fp:
		writer = csv.writer(fp, delimiter=delimiter, dialect='excel')
		writer.writerow(headers)
		for r in rows:
			writer.writerow(r)

def accessions_to_country(input_file):
	accessions = {}
	with open(input_file, 'r') as fp:
		reader=csv.reader(fp, delimiter="\t")
		for r in reader:
			if "run_accession" not in r:
				accessions.update({r[0]: r[1]})
	return accessions



def main(args):
	accessions_country = accessions_to_country("countries.txt")
	# print(accessions_country["ERR1713335"])
	# exit()
	files = glob.glob(os.path.join(args.directory,"*"))
	# get headers
	# headers = [""]
	# for f in files:
	#     with open(f, 'r') as fp:
	#         i = csv.reader(fp, delimiter='\t')
	#         o_f_path, o_f_name = os.path.split(os.path.abspath(f))
	#         filename = o_f_name.split(".gene_mapping_data.txt")[0]
	#         for line in i:
	#         	if "ARO Term" not in line:
	#         		items = line[24].split(";")
	#         		for i in items:
	#         			if i not in headers:
	#         				headers.append(i)

	# get isolates by drug class
	# isolates = {}
	# for f in files:
	#     with open(f, 'r') as fp:
	#         i = csv.reader(fp, delimiter='\t')
	#         o_f_path, o_f_name = os.path.split(os.path.abspath(f))
	#         filename = o_f_name.split(".gene_mapping_data.txt")[0]
	#         for line in i:
	#         	if "ARO Term" not in line:#and line[12] == "100.00":
	#         		# print(filename, " - ", line[12], " -> ",line[24])
	#         		items = line[24].split(";")
	#         		for c in items:
	#         			if filename not in isolates.keys():
	#         				isolates[filename] = {c: line[12]}
	#         			else:
	#         				isolates[filename][c] = line[12]


	# write tsv
	
	# with open("out.txt", 'w') as fp:
	# 	writer = csv.writer(fp, delimiter=',', dialect='excel')
	# 	writer.writerow(headers)
	# 	for i in isolates:
	# 		row = []
	# 		row.append(i)
	# 		for h in headers:
	# 			if h not in [""]:
	# 				if h in isolates[i].keys():
	# 					row.append(isolates[i][h])
	# 				else:
	# 					row.append(0)
	# 		writer.writerow(row)
	# field = 12
	field = 9
	headers = get_headers(files, 24)
	isolates = get_isolates_alt(files, 24, field)
	# for i in isolates:
	# 	for c in isolates[i].keys():
	# 		if "sul" in c:
	# 			print(c, isolates[i][c])
	# 			# print(isolates[i])
	write_csv("out_drug_class_original_names.txt", headers, isolates, accessions_country)

	# headers = get_headers(files, 24)
	# isolates = get_isolates(files, 24, field)
	# write_csv("out_drug_class_original_names.txt", headers, isolates, accessions_country)

	headers = get_headers(files, 23)
	isolates = get_isolates_alt(files, 23, field)
	write_csv("out_amr_gene_family_original_names.txt", headers, isolates, accessions_country)

	headers = get_headers(files, 25)
	isolates = get_isolates_alt(files, 25, field)
	write_csv("out_resistance_mechanism_original_names.txt", headers, isolates, accessions_country)

	headers = get_headers(files, 0)
	isolates = get_isolates(files, 0, field)
	write_csv("out_genes_original_names.txt", headers, isolates, accessions_country)
	# print("genes: {}".format(len(headers)))

	trim_headers("out_drug_class_original_names.txt","out_drug_class.txt")
	trim_headers("out_amr_gene_family_original_names.txt","out_amr_gene_family.txt")
	trim_headers("out_resistance_mechanism_original_names.txt","out_resistance_mechanism.txt")
	trim_headers("out_genes_original_names.txt","out_genes.txt")


def create_parser():
	parser = argparse.ArgumentParser(prog="create_data", description="{}".format("heatmap data"))
	parser.add_argument('-i', '--directory', required=False, help='input directory')
	return parser

def run():
	parser = create_parser()
	args = parser.parse_args()
	main(args)

if __name__ == "__main__":
	run()
