import sys
from Bio import SeqIO
from re import finditer
import re
import urllib

file = open(sys.argv[1])

protein = {}

for lines in file:
	ptn_id = lines.strip().split('_')[0]
	url = 'http://www.uniprot.org/uniprot/{0}.fasta'.format(ptn_id)
	file = urllib.urlopen(url)
	seq = SeqIO.parse(file,'fasta')
	for line in seq:
		identity = line.id.split('|')[1]
		protein[identity] = line.seq
		
#motif = re.compile(r'(?=(N[^P][ST][^P]))')


for name, seq in protein.items():
	motif = re.compile('N(?=[^P][ST][^P])')
	index = 0
	out = []
	a = str(seq)
	while (index <len(a)):
		index += 1
		if re.search(motif, a[index:]) == None:
			break
		elif re.match(motif, a[index:]) != None:
			out.append(index+1)
	if out != []: #do not print empty list
		print(name)
		print(' '.join([ str(i) for i in out]))
	



#	a = str(seq)
#	print(name, a)
#	for m in motif.finditer(a):
#		print (m.start()+1)