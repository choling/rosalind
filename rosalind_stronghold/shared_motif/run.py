import sys
from Bio import SeqIO

file = sys.argv[1]
file_seq = SeqIO.parse(file,'fasta')


seq = {}
seq_id = ''
 
for lines in file_seq:
	seq[lines.id]=lines.seq

#for lines in file_seq:
#	if lines[0] == '>':
#		seq_id = lines.rstrip()
#		seq[seq_id] = ''
#		continue
#	else:
#		seq[seq_id] += (lines.rstrip()).upper()


dna = []

for sequence in seq:
	dna.append(seq[sequence])


def checksubstring(find_string, dna):
        for string in dna:
                if (len(string) < len(find_string)) or (find_string not in string):
                    return False
        return True


longest_dna = ''

for start_index in range(len(dna[0])):
    for end_index in range(len(dna[0]), start_index, -1):
    	# Break if the length becomes too small, as it will only get smaller.
        if end_index - start_index <= len(longest_dna):
            break
        elif checksubstring(dna[0][start_index:end_index], dna):
            longest_dna =  dna[0][start_index:end_index]

 


print(longest_dna)