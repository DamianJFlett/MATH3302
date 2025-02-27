#affine cipher
#first attempt -frequency analysis
from collections import defaultdict
from cipher_tools import Affine_Cipher,  Affine_Solver
ciphertext = "OGHYLXEEQOGWNYJYGHYNKESOETHFYOGLOGHYLXEEPLEIQWYHEXEDYKESJELYDYLIELY"
#context - affine. find a, b

#First, try brute force.
s = Affine_Solver()
s.brute_force(ciphertext, decrypt = True)
#a=11, b=6 produces an intelligible message
counts = defaultdict(int)
for c in ciphertext:
    counts[c]+=1
print("counts are", counts)


def key_fn(t1):
    return t1[1]

counts_sorted = sorted(counts.items(), key=key_fn, reverse = True)
print(counts_sorted)

#most common are E, Y, then drop off until L
#to try: (E <- e, Y<- t), (E <- t, Y<- e). Furthermore, try fitting A or R in if neither works

#pow(x, y, p) returns x^y mod p!

#denote |x| = z's imagine in z_26 under {(0, a), ....}
#a|e|+b=|E|
#a|t|+b=|Y|

#therefore, a(|e|-|t|) = |E|-|Y|
#a = (|E|-|Y|)(|e|-|t|)^{-1}

print("a in first case would be ")
