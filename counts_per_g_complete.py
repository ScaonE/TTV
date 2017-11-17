#!/usr/bin/env python
import os
import sys

usage = '\t --------\n' \
        '\t| usage  : python counts_per_g_complete.py file_1\n' \
        '\t| input  : file_1 = blastn_vs_viralDB.tsv\n' \
        '\t| output : counts_per_g_complete.tsv\n' \
        '\t --------'

if len(sys.argv) != 2:
    print(usage)
    sys.exit()

ttv_g_dic = {
             'NC_015783.1': 0, 'NC_014480.2': 0, 'NC_014096.1': 0,
             'NC_014094.1': 0, 'NC_014091.1': 0, 'NC_014084.1': 0,
             'NC_014083.1': 0, 'NC_014081.1': 0, 'NC_014080.1': 0,
             'NC_014079.1': 0, 'NC_014078.1': 0, 'NC_014077.1': 0,
             'NC_014076.1': 0, 'NC_014075.1': 0, 'NC_014074.1': 0,
             'NC_014073.1': 0, 'NC_014069.1': 0, 'NC_002076.2': 0,
             'KP343839.1': 0, 'KP036971.1': 0, 'AY823989.1': 0,
             'AY823988.1': 0
}

query_set = set()  # query = read
with open(sys.argv[1], 'r') as tsv:
    for row in tsv:
        columns = row.split('\t')
        qseqid, sseqid = columns[0], columns[1]
        if qseqid not in query_set:  # we encounter the first = best hit for this read
            query_set.add(qseqid)  # won't investigate next hits for this read
            accession_number = sseqid.replace('ref', '').replace('|', '')
            if accession_number in ttv_g_dic:
                ttv_g_dic[accession_number] += 1

file = sys.argv[1].split('/')
sample = file[-1].split('_')[0]
header, results = ['Sample\t'], [sample + '\t']

for k, v in sorted(ttv_g_dic.items(), reverse=True):
    header.append(str(k) + "\t")
    results.append(str(v) + "\t")
header.append('\n')
results.append('\n')

if not os.path.isfile('counts_per_g_complete.tsv'):
    with open('counts_per_g_complete.tsv', 'a') as out:
        for i in header:
            out.write(i)
        for i in results:
            out.write(i)
else:
    with open('counts_per_g_complete.tsv', 'a') as out:
        for i in results:
            out.write(i)
