from Bio.Seq import Seq

f = open('rosalind_revc.txt','r')
d = f.read()

seq = ''

for line in d:
	for a in line:
		seq += a

a = Seq(seq)
rev = a.reverse_complement()
print rev

