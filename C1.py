#affine cipher
#first attempt -frequency analysis
from collections import defaultdict
from cipher_tools import Affine_Cipher,  Affine_Solver,Caesar_Cipher
ciphertext = "OGHYLXEEQOGWNYJYGHYNKESOETHFYOGLOGHYLXEEPLEIQWYHEXEDYKESJELYDYLIELY"
#context - affine. find a, b

#First, try brute force.

s1 = "FJNZCJNYYNOL"
s = Caesar_Cipher(3)
s.brute_force(s1, 1)
s = Affine_Solver()
s.brute_force(ciphertext, decrypt = True)
#a=11, b=6 produces an intelligible message, after seeing the consolve 
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
#
print(s.solve_affine([("e", "E"), ("t", "Y")]))
print(s.solve_affine([("t", "E"), ("e", "Y")]))
#both solutions here are nonviable as a is not coprime with 26. In addition, they dont agree with the brute force answer.
#doing some whitebox-ish testing, the most common letter in the plaintext string is actually o, the fourth most common letter in the english langugage.
#This is why frequency analysis is not perfect: we would have had to try quite a few more combinations of most common ciphertext letters before we got to o, 
#so in this case it might have been more demonstrative to use frequency analysis ot just determine in what order to brute force, if operations were more complex.
#TODO - check if this is more computationally efficient in any way. (this might be useful in mixed-alpha)
#  For the sake of demonstrating the solver though:
print(s.solve_affine([("o", "E"), ("e", "Y")]))
