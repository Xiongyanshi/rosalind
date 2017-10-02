#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Bio import SeqIO


def parse_fasta_to_matrix(file_path):
    '''return the sequence base matrix for a give alignment fasta file,
    discard sequence name'''
    record = SeqIO.parse(file_path, 'fasta')
    seq_matrix = []
    for entry in record:
        seq_matrix.append(str(entry.seq))
    return seq_matrix


def consensus_base(dna_seq):
    '''return the most consensus base in a given loci, dna_seq'''
    maxx = 0
    result = ''
    dna_seq = dna_seq.upper()
    for i in 'ATCG':
        if dna_seq.count(i) > maxx:
            maxx = dna_seq.count(i)
            result = i
    return result


def seq_matrix_to_profile(seq_matrix):
    a_list = []
    c_list = []
    g_list = []
    t_list = []
    consensus_seq = ''
    for i in range(len(seq_matrix[0])):
        row_i = ''
        for j in seq_matrix:
            row_i += j[i]
        a_list.append(row_i.count('A'))
        c_list.append(row_i.count('C'))
        g_list.append(row_i.count('G'))
        t_list.append(row_i.count('T'))
        consensus_seq += consensus_base(row_i)
    return {'con': consensus_seq,
            'A': a_list,
            'C': c_list,
            'G': g_list,
            'T': t_list}


def main():
    sequence_matrix = parse_fasta_to_matrix(sys.argv[1])
    seq_profile = seq_matrix_to_profile(sequence_matrix)
    print seq_profile['con']
    for base in 'ACGT':
        base_profile = ''.join([str(i) + ' ' for i in seq_profile[base]])
        print '{}: {}'.format(base, base_profile)


if __name__ == '__main__':
    main()
