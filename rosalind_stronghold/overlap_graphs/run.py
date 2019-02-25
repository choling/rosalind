from Bio import SeqIO

seq = SeqIO.parse('rosalind_grph.txt','fasta')

data = {}

for s in seq:
	data[s.id] = s.seq

overlapped_id = []
overlapped_seq = []

for k1,v1 in data.items():
	for k2,v2 in data.items():
		if k1 != k2 and v1[-3:] == v2[:3]:
			overlapped_id.append(k1+' '+k2)
			overlapped_seq.append(v1+' '+v2)

for lines in overlapped_id:
	print(lines)