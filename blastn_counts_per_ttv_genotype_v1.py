#!/usr/bin/env python
import os
import sys

usage = '\t --------\n' \
		'\t| usage  : python blastn_counts_per_ttv_genotype file_1\n' \
		'\t| input  : file_1 = blastn_vs_viralDB.tsv\n' \
		'\t| output : read_count_per_genotypes.tsv\n' \
		'\t --------'

if len(sys.argv) != 2:
	print(usage)
	sys.exit()

ttv_genotypes_dic = {
	'AB038621.1': 0, 'AB049607.1': 0, 'AB060594.1': 0, 'AB060597.1': 0, 'AF345523.1': 0, 'AF345524.1': 0, 'AF345526.1': 0, 'AF348409.1': 0, 'AX025718.1': 0, 'AX025830.1': 0, 'AX174942.1': 0, 'AY823988.1': 0, 'AY823989.1': 0, 'DQ187006.1': 0, 'KP036971.1': 0, 'KP343839.1': 0, 'KT163875.1': 0, 'KT163876.1': 0, 'KT163879.1': 0, 'KT163880.1': 0, 'KT163882.1': 0, 'KT163885.1': 0, 'KT163886.1': 0, 'KT163887.1': 0, 'KT163893.1': 0, 'KT163896.1': 0, 'KT163897.1': 0, 'KT163898.1': 0, 'KT163900.1': 0, 'KT163901.1': 0, 'KT163903.1': 0, 'KT163904.1': 0, 'KT163905.1': 0, 'KT163906.1': 0, 'KT163911.1': 0, 'KT163912.1': 0, 'KT163915.1': 0, 'KT163916.1': 0, 'KT163917.1': 0, 'NC_002076.2': 0, 'NC_014069.1': 0, 'NC_014073.1': 0, 'NC_014074.1': 0, 'NC_014075.1': 0, 'NC_014076.1': 0, 'NC_014077.1': 0, 'NC_014078.1': 0, 'NC_014079.1': 0, 'NC_014080.1': 0, 'NC_014081.1': 0, 'NC_014083.1': 0, 'NC_014084.1': 0, 'NC_014091.1': 0, 'NC_014094.1': 0, 'NC_014096.1': 0, 'NC_014480.2': 0, 'NC_015783.1': 0 
	}

query_set = set() # query = read
with open(sys.argv[1], 'r') as tsv:
	for row in tsv:
		columns = row.split('\t')
		qseqid, sseqid = columns[0], columns[1]
		if qseqid not in query_set: # we encounter the first = best hit for this read
			query_set.add(qseqid) # won't investigate next hits for this read
			accession_number = sseqid.replace('ref', '').replace('|', '')
			if accession_number in ttv_genotypes_dic:
				ttv_genotypes_dic[accession_number]+=1

file = sys.argv[1].split('/')
sample = file[-1].split('_')[0]
header, results = ['Sample\t'], [sample+'\t']

for k, v in sorted(ttv_genotypes_dic.items(), reverse=True):
	header.append(str(k)+"\t")
	results.append(str(v)+"\t")
header.append('\n')
results.append('\n')

if not os.path.isfile('read_count_per_genotypes.tsv'):
	with open('read_count_per_genotypes.tsv', 'a') as out:
		for i in header:
			out.write(i)
		for i in results:
			out.write(i)
else:
	with open('read_count_per_genotypes.tsv', 'a') as out:
		for i in results:
			out.write(i)
