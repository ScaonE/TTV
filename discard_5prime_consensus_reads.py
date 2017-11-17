#!/usr/bin/env python
import os
import sys

usage = '\t --------\n' \
        '\t| usage  : python discard_5prime_consensus_reads file_1\n' \
        '\t| input  : file_1 = blastn_vs_5prime_consensus.tsv\n' \
        '\t| output : a file containing read names to discard\n' \
        '\t --------'

if len(sys.argv) != 2:
    print(usage)
    sys.exit()

query_dic = {}
with open(sys.argv[1], 'r') as tsv:
    for row in tsv:
        columns = row.split('\t')
        qseqid, length, qstart, qend, sstart, send, qlen, sstrand = columns[0], int(columns[3]), int(
            columns[6]), int(columns[7]), int(columns[8]), int(columns[9]), int(columns[12]), columns[14].rstrip()
        if not qseqid in query_dic:
            if length >= 25:
                if sstrand == 'plus':
                    five_prime_overhead = (qstart - 1) - (sstart - 1) - 67
                    three_prime_overhead = (qlen - qend) - (93 - send)
                elif sstrand == 'minus':
                    five_prime_overhead = (qlen - qend) - (send - 1) - 67
                    three_prime_overhead = (qstart - 1) - (93 - sstart)
                else:
                    print('------------ERROR------------')
                if five_prime_overhead >= 50 or three_prime_overhead >= 50:
                    query_dic[qseqid] = 'keep'
                else:
                    query_dic[qseqid] = 'discard'

file = sys.argv[1].split('/')
sample = file[-1].split('.')[0]

with open(sample + '.discard', 'a') as out:
    for k, v in query_dic.items():
        if v == 'discard':
            out.write(k + "\n")
