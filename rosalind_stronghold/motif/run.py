f = open('rosalind_subs.txt','r')
d = f.readlines()

s = d[0].strip()
t = d[1].strip()

i = 0

while i < (len(s)-len(t)):
	if s[i:i+len(t)] == t:
		print i+1
	i += 1



