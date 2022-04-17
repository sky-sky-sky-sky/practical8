from asyncore import write
import re
a=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#open the file
b=open('cut_genes.fa','w')
c=a.read()
gene_all=re.compile(r'gene:(\S+).*?](.*?)>',re.S)#find gene name and gene sequence
gene=gene_all.findall(c)
for i in range(len(gene)):
    d=re.sub(r'\n','',gene[i][1])
    if 'GAATTC' in d:#find the gene that have GAATTC
        b.write('>')
        b.write(gene[i][0]+'           ')
        b.write(str(len(d))+'\n')
        b.write(d+'\n')#write the gene in the file
b.close()
a.close()

