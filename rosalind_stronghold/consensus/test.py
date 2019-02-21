from Bio import SeqIO
from collections import Counter

seq_all = SeqIO.parse('rosalind_cons.txt','fasta')

length = 0

seq = {}

for rec in seq_all:
     #print rec.id, rec.seq[0]
	  length = len(rec.seq)
	  seq[rec.id] = rec.seq

A = []
C = []
G = []
T = []
consensus_seq = ''

for i in range(length):
	lines = ''
	number_seq += 1
	for k in seq.keys():
		lines += seq[k][i]
	A.append(lines.count('A'))
	C.append(lines.count('C'))
	G.append(lines.count('G'))
	T.append(lines.count('T'))
	seq_count += 1
	counts = Counter(lines)
	consensus_seq += counts.most_common()[0][0]

print (consensus_seq)
print ('\n'.join(['A:\t'+'\t'.join(map(str,A)), 'C:\t'+'\t'.join(map(str,C)),'G:\t'+'\t'.join(map(str,G)), 'T:\t'+'\t'.join(map(str,T))]))

