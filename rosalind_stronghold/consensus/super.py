from Bio import SeqIO

seq_all = SeqIO.parse('test.txt','fasta')

sequences = []
for rec in seq_all:
	sequences.append(rec.seq)
length = len(sequences[0])

count_nt = [{} for i in range(length)]

for sequence in sequences:
	for i,ch in enumerate(sequence):
		if ch in count_nt[i]:
			count_nt[i][ch] += 1
		else:
			count_nt[i][ch] = 1
#print count_nt

for a in count_nt:
	print a			
