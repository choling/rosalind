import urllib
import re
import collections

#returns dna sequence without the GI header
def readSeq(FASTA):
    for line in FASTA:
        if line.startswith('>'):
            continue
        clean = line.strip()
        return clean

with file('rosalind_mprt.txt', 'r') as data:
    proteinnames = data.read().strip().split()

motif = re.compile('N(?=[^P][ST][^P])') #using a look ahead to make sure overlapping matches are found

#retrieves and stores the sequences in a list
seqlist = []
a = []
for name in proteinnames:
    url = 'http://www.uniprot.org/uniprot/{0}.fasta'.format(name)
    filedata = urllib.urlopen(url)
    lines = filedata.readlines()
    a = lines[1:]
    clean = ''.join(a).replace('\n', '')
    seqlist.append(clean.strip())

#attches protein name with associated sequence and binds them within a dictionary
id_seq = dict(zip(proteinnames, seqlist))


keys = []
dna = []
for key, seqs in id_seq.items():
    temp = []
    if re.search(motif, seqs):
        keys.append(key)  #will only append proteins that have the motif
    for find in [find.start() + 1 for find in re.finditer(motif, seqs)]:  
        if re.search(motif, seqs):
            temp.append(find)  #failsafe to insure only matches with the motif append
    if len(temp) != 0:  #insures that an empty list doesn't get appended
        crimp = ''.join(str(temp))
        dna.append(crimp.replace('[', '').replace(']', '').replace(',', '').strip())
# perhaps I should using izip to reduce memory impact
ordered_dict = dict(zip(keys, dna))  #binds the stored protein names with there associated sequences
od = collections.OrderedDict(sorted(ordered_dict.items()))  #sorts the list alphabetically by key value

for k, v in od.items():
    print k
    print v