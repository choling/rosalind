f = open('rosalind_hamm.txt','r')
seqs = f.readlines()
f.close()

s = seqs[0].strip()
t = seqs[1].strip()

point_seq_s = []
point_seq_t = []
point_pos = 0
 
if len(s) != len(t):
	print('Error: DNA strands not the same length')
else:
	for i in range(len(s)):
		if s[i] != t[i]:
			point_seq_s.append(s[i])
			point_seq_t.append(t[i])
			point_pos += 1
print point_seq_s
print point_seq_t
print point_pos
	
