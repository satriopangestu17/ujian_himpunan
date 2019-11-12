A = {2,4,6,8,10,12,14,16,18}
B = {1,3,5,7,9,11,13,15,17,19}
C = {-9,-8,-7,-6,-5,-4,-3,-2,-1}
D = {2,3,5,7,11,13,17,19}
E = {4,6,8,9,10,12,14,15,16,18}

#soal a. A ∪ B ∪ C ∪ D ∪ E
print(A|B|C|D|E)

#soal b. (A ∩ B) ∪ (D ∩ E)
AiB = (A&B)
DiE = (D&E)
print((A&B|D&E))


#soal c. (A ∪ B) ∩ (D ∪ E)
print((A|B)&(D|E))

#soal d. (A ∪ B) - (D ∪ E)
print((A|B)-(D|E))

#soal e. (A ∪ B ∪ C) - (A ∩ E)
print((A|B|C)-(A&E))
