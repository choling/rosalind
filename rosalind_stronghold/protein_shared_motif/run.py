import sys
from Bio import SeqIO
from re import finditer
import re
import urllib

file = open(sys.argv[1])

protein = {}

for lines in file:
	ptn_id = lines.strip()
	url = 'http://www.uniprot.org/uniprot/{0}.fasta'.format(ptn_id)
	file = urllib.urlopen(url)
	seq = SeqIO.parse(file,'fasta')
	for line in seq:
#		print(line.id)
#		print(line.seq)
		protein[line.id] = line.seq
#print(protein)
		
motif = re.compile(r'(?=(N[^P][ST][^P]))')



for name, seq in protein.items():
	a = str(seq)
	print(name)
	for m in motif.finditer(a):
		print (m.start()+1)