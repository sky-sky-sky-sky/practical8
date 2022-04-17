seq='ATGCAATCGACTACGATCAATCGAGGGCC'
b=seq.split('GAATTC')#split GAATTC
c=list(b)
d=['']
for i in c:
    if i in d:
        b.remove(i)
a=len(b)
e=list(seq)
if e[-6:-1]==['A', 'G', 'G', 'G', 'C']:# if the GAATTC on the last of the sequence
    a=a+1
print('total number of fragments is',a)
        