codon_table = {
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 
'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S', 
'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 
'AUU':'I', 'AUC':'I', 'AUA':'I', 'UUA':'L', 
'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',  
'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 
'GGG':'G', 'GUU':'V', 'GUC':'V', 'GUA':'V', 
'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T', 
'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 
'CCG':'P', 'AAU':'N', 'AAC':'N', 'GAU':'D', 
'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',  
'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 
'CAC':'H', 'AAA':'K', 'AAG':'K', 'UUU':'F', 
'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
'UGG':'W', 'UAG':'', 'UGA':'', 'UAA':''
}

def trans (seq):
        i = 0
        p = ""
        while i < len(seq)/3 - 1:
                n = seq[3*i]+seq[3*i+1]+seq[3*i+2]
                r = codon_table[n]
                i += 1
                p = p + r
        return p

f = open('rosalind_prot.txt','r')
a = f.read()

peptide = trans(a)

print(peptide)

#https://www.bilibili.com/read/cv1997726
