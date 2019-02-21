from Bio import SeqIO
from Bio.SeqUtils import GC


all = SeqIO.parse('rosalind_gc.txt','fasta')

current_id = 0
current_gc = 0
highest_id = 0
highest_gc = 0


for rec in all:
	current_id = rec.id 
	current_gc = GC(rec.seq)
	if current_gc > highest_gc:
		highest_gc = current_gc
		highest_id = current_id

print highest_id 
print highest_gc
