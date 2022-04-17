import re
print('please write the filename for the fasta file with .fasta')
filename=input()
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#open the file
b=open(filename,'w')#found the new file 
c=a.read()
gene_all=re.compile(r'gene:(\S+).*?](.*?)>',re.S)#find gene name and gene sequence
gene=gene_all.findall(c)
for i in range(len(gene)):
    d=re.sub(r'\n','',gene[i][1])
    if 'GAATTC' in d:#find what we want
        e=d.split('GAATTC')
        f=list(e)
        g=['']
        for i in f:
            if i in g:
                f.remove(i)
        h=len(b)
        j=list(gene[i][1])
        if j[-6:-1]==['A', 'G', 'G', 'G', 'C']:# if the GAATTC on the last of the sequence
            h=h+1
        b.write('>')
        b.write(gene[i][0]+'\n')
        b.write('total number of fragments is'+h)
b.close()
a.close()