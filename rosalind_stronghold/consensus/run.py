from Bio import SeqIO

seq_all = SeqIO.parse('test.txt','fasta')

length = 0

for rec in seq_all:
#	print rec.id, rec.seq
	length = len(rec.seq)

pos = 0

row_a = [0]*length
row_t = [0]*length
row_c = [0]*length
row_g = [0]*length

while (pos < length):
	for line in seq_all:
		print a.seq
	pos += 1

print row_a
print row_t
print row_c
print row_g
