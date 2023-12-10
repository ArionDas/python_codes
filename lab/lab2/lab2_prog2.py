# if the given string is S="Johny Johny yes Pappa", determine the following:
# total length
# the first occ of 'y'
# total number of occ of 'y'
# generate "Johny Johny yes Mummy" 

S = "Johny Johny yes Pappa"
print(len(S))
first_occ = 0
occ = 0
cnt = 0
for i in S:
    if(first_occ == 0 and i == 'y'):
        first_occ = cnt
    if(i == 'y'):
        occ += 1
    occ += 1
    cnt += 1

S2 = S[:-5] + "Mummy"
print(S2)
