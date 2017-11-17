#!/usr/bin/env python
import os
import sys
from matplotlib import pyplot

usage = '\t --------\n' \
        '\t| usage  : python counts_orf1.py file_1\n' \
        '\t| input  : file_1 = blastn_vs_viralDB.tsv\n' \
        '\t| output : counts_per_orf1.tsv\n' \
        '\t| output : folders with plots\n' \
        '\t --------'

if len(sys.argv) != 2:
    print(usage)
    sys.exit()

ttv_g_dic = {
    'AB038621.1': [0, 665, 2867], 'AB049607.1': [0, 596, 3074],
    'AB060594.1': [0, 503, 2756], 'AB060597.1': [0, 507, 2808],
    'AF345523.1': [0, 1049, 2768], 'AF345524.1': [0, 479, 2708],
    'AF345526.1': [0, 766, 2836], 'AF348409.1': [0, 454, 2677],
    'AX025718.1': [0, 578, 2828], 'AX025830.1': [0, 581, 2864],
    'AX174942.1': [0, 811, 2923], 'AY823988.1': [0, 597, 2841],
    'AY823989.1': [0, 603, 2934], 'DQ187006.1': [0, 622, 2851],
    'KP036971.1': [0, 538, 2779], 'KP343839.1': [0, 500, 2705],
    'KT163875.1': [0, 620, 2900], 'KT163876.1': [0, 481, 2485],
    'KT163879.1': [0, 578, 2834], 'KT163880.1': [0, 582, 2922],
    'KT163882.1': [0, 504, 2472], 'KT163885.1': [0, 101, 2366],
    'KT163886.1': [0, 592, 2938], 'KT163887.1': [0, 544, 2866],
    'KT163893.1': [0, 568, 2893], 'KT163896.1': [0, 629, 2873],
    'KT163897.1': [0, 850, 2779], 'KT163898.1': [0, 202, 2224],
    'KT163900.1': [0, 350, 2663], 'KT163901.1': [0, 491, 2801],
    'KT163903.1': [0, 599, 2927], 'KT163904.1': [0, 591, 2799],
    'KT163905.1': [0, 558, 2856], 'KT163906.1': [0, 570, 2796],
    'KT163911.1': [0, 603, 2841], 'KT163912.1': [0, 477, 2769],
    'KT163915.1': [0, 587, 2927], 'KT163916.1': [0, 578, 2894],
    'KT163917.1': [0, 542, 2738], 'NC_002076.2': [0, 588, 2901],
    'NC_014069.1': [0, 594, 2802], 'NC_014073.1': [0, 486, 2691],
    'NC_014074.1': [0, 561, 2799], 'NC_014075.1': [0, 604, 2839],
    'NC_014076.1': [0, 611, 2849], 'NC_014077.1': [0, 622, 2920],
    'NC_014078.1': [0, 594, 2832], 'NC_014079.1': [0, 692, 2891],
    'NC_014080.1': [0, 607, 2908], 'NC_014081.1': [0, 580, 2791],
    'NC_014083.1': [0, 676, 2848], 'NC_014084.1': [0, 591, 2829],
    'NC_014091.1': [0, 591, 2877], 'NC_014094.1': [0, 597, 2757],
    'NC_014096.1': [0, 590, 2855], 'NC_014480.2': [0, 388, 2572],
    'NC_015783.1': [0, 562, 2767]
}

g_pileup_dic = {
    'AB038621.1': [0] * 3676, 'AB049607.1': [0] * 3301, 'AB060594.1': [0] * 3234,
    'AB060597.1': [0] * 3246, 'AF345523.1': [0] * 3229, 'AF345524.1': [0] * 3193,
    'AF345526.1': [0] * 3312, 'AF348409.1': [0] * 3153, 'AX025718.1': [0] * 3313,
    'AX025830.1': [0] * 3249, 'AX174942.1': [0] * 3847, 'AY823988.1': [0] * 3816,
    'AY823989.1': [0] * 3920, 'DQ187006.1': [0] * 3064, 'KP036971.1': [0] * 3599,
    'KP343839.1': [0] * 3551, 'KT163875.1': [0] * 3275, 'KT163876.1': [0] * 2650,
    'KT163879.1': [0] * 3748, 'KT163880.1': [0] * 3225, 'KT163882.1': [0] * 2792,
    'KT163885.1': [0] * 3300, 'KT163886.1': [0] * 3333, 'KT163887.1': [0] * 2996,
    'KT163893.1': [0] * 3218, 'KT163896.1': [0] * 3451, 'KT163897.1': [0] * 3014,
    'KT163898.1': [0] * 2958, 'KT163900.1': [0] * 2922, 'KT163901.1': [0] * 3141,
    'KT163903.1': [0] * 3276, 'KT163904.1': [0] * 3158, 'KT163905.1': [0] * 3177,
    'KT163906.1': [0] * 3153, 'KT163911.1': [0] * 3168, 'KT163912.1': [0] * 3060,
    'KT163915.1': [0] * 3226, 'KT163916.1': [0] * 3190, 'KT163917.1': [0] * 3046,
    'NC_002076.2': [0] * 3852, 'NC_014069.1': [0] * 3690, 'NC_014073.1': [0] * 3629,
    'NC_014074.1': [0] * 3729, 'NC_014075.1': [0] * 3759, 'NC_014076.1': [0] * 3770,
    'NC_014077.1': [0] * 3899, 'NC_014078.1': [0] * 3808, 'NC_014079.1': [0] * 3798,
    'NC_014080.1': [0] * 3736, 'NC_014081.1': [0] * 3748, 'NC_014083.1': [0] * 3763,
    'NC_014084.1': [0] * 3790, 'NC_014091.1': [0] * 3818, 'NC_014094.1': [0] * 3705,
    'NC_014096.1': [0] * 3787, 'NC_014480.2': [0] * 3322, 'NC_015783.1': [0] * 3725
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
                sstart, send = columns[8], columns[9]
                min_subject = min(int(sstart), int(send))
                max_subject = max(int(sstart), int(send))
                # max_subject + 1 cause out of range errors
                if (min_subject + 50) in range(ttv_g_dic[accession_number][1], ttv_g_dic[accession_number][2] + 1):
                    ttv_g_dic[accession_number][0] += 1
                for i in range(min_subject, max_subject):
                    g_pileup_dic[accession_number][i] += 1

file = sys.argv[1].split('/')
sample = file[-1].split('_')[0]

# Create counts_per_orf1.tsv (fill it with each new TSV analysed)
header, results = ['Sample\t'], [sample + '\t']

for k, v in sorted(ttv_g_dic.items(), reverse=True):
    header.append(str(k) + "\t")
    results.append(str(v[0]) + "\t")
header.append('\n')
results.append('\n')

if not os.path.isfile('../counts_per_orf1.tsv'):
    with open('../counts_per_orf1.tsv', 'a') as out:
        for i in header:
            out.write(i)
        for i in results:
            out.write(i)
else:
    with open('../counts_per_orf1.tsv', 'a') as out:
        for i in results:
            out.write(i)

for k, v in g_pileup_dic.items():
    if sum(v) >= 1000:
        pyplot.plot(v)
        pyplot.axvspan(ttv_g_dic[k][1], ttv_g_dic[k]
                       [2], color='grey', alpha=0.25)
        pyplot.title(k + ' (orf1 in grey)')
        pyplot.ylabel('Depth')
        pyplot.xlabel('Position')
        pyplot.savefig(k + '.png')
        pyplot.clf()
