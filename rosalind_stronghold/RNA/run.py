

f=open('rosalind_rna.txt','r')
d=f.read()

#print(d)

seq=''
for line in d:
	for a in line:
		if a == 'T':
			seq += 'U'
			#seq.append(a)
		else:
			seq += a

#print(seq)

#for i in seq:
#	print i,

with open('result.txt','w') as r:
	r.write(seq)
