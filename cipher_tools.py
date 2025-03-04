from collections import defaultdict
import math
from itertools import permutations
import numpy as np

LATIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Cipher():
    def __init__(self, alphabet:str = LATIN_ALPHABET):
        self._alphabet_size = len(alphabet)
        self._numerise = {}
        self._letterise = {}
        self._alphabet = alphabet
        #generate a mapping from z_n to the alphabet and vice versa
        i = 0
        for c in alphabet:
            self._letterise[i % self._alphabet_size] = c.lower()
            self._numerise[c.upper()] = i % self._alphabet_size
            self._numerise[c.lower()] = i % self._alphabet_size
            i += 1
    def encrypt(self, message:str) -> str:
        """
        Encrypts the given message using the cipher. If a letter not in the alphabet is used, it will remain where it was, unencrypted.
        """
        pass
    def decrypt(self, message:str) -> str:
        """
        Decrypts the given message using the cipher. If a letter not in the alphabet is used, it will remain where it was, undecrypted.
        """
        pass
    def freqs(self, message:str, print = False) -> str:
        """
        Prints out frequences of each letter in the given message, and compares it to frequencies in the english language. Does not support 
        non-english languages or alphabets other than the 26 letters of the latin alphabet. 
        """
        l = len(message)
        #lol
        upper = {c.upper(): (message.count(c.lower())+message.count(c.upper()))/l for c in LATIN_ALPHABET}
        lower = {c.lower(): (message.count(c.lower())+message.count(c.upper()))/l for c in LATIN_ALPHABET}
        freqs = dict(upper, **lower)
        if print:
            pass
        return freqs
        
#TODO (Maybe): subcategorise ciphers - some, each letter will go to exactly one other letter under the en/decryption mapping, those can be refactored into one superclass 
#which always checks for nonalphabet characters, thus reducing some repitition
class Affine_Cipher(Cipher):
    """
    A cipher with key (a,b) and encryption function e(x)=ax+b
    Precondition: gcd(a, 26) == 1
    """
    def __init__(self, a: int, b: int, alphabet:str = LATIN_ALPHABET):
        if math.gcd(a, len(alphabet)) != 1:
            raise ValueError("Uh-Oh! a was not coprime with the alphabet size.")
        super().__init__(alphabet)
        self._a = a
        self._b = b

    def encrypt(self, message: str) -> str:
        encrypted = ""
        for c in message:
            if c in self._numerise :
                encrypted += self._letterise[(self._a * self._numerise[c]+self._b) % self._alphabet_size]
            else:
                encrypted += c
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = ""
        for c in message:
            if c in self._numerise:
                decrypted += self._letterise[((pow(self._a,-1,self._alphabet_size)) * (self._numerise[c] - self._b)) % self._alphabet_size]
            else:
                decrypted += c
        return decrypted.lower()

class Caesar_Cipher(Cipher):
    """
    A cipher with a key, shift k. The encryption function is e(x)=x+k
    """
    def __init__(self, shift: int, alphabet:str = LATIN_ALPHABET):
        super().__init__(alphabet)
        self._shift = shift

    def encrypt(self, message: str) -> str:
        encrypted = "" 
        for c in message:
            if c in self._numerise:
                encrypted += self._letterise[(self._numerise[c]+ self._shift)% self._alphabet_size]
            else:
                encrypted += c
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = "" 
        for c in message:
            if c in self._numerise:
                decrypted += self._letterise[(self._numerise[c]- self._shift) % self._alphabet_size]
            else:
                decrypted += c
        return decrypted.lower()

class MixedAlphabetCipher(Cipher):
    def __init__(self, alphabet:str = LATIN_ALPHABET):
        super().__init__()
    def solve(self):
        pass #TODO: need some way to pass permutations as input for an arbitrary list ideally, and then parse those

class HillCipher(Cipher):
    def __init__(self, key: list[list[int]], alphabet: str = LATIN_ALPHABET):
        super().__init__()
        if any(len(key) == len(key[n]) for n in range(len(key))):
            raise ValueError("Provided key was not square!")
        #check if the matrix is invertible
        if np.linalg.matrix_rank(key) != len(key):
            raise ValueError("Provided key was singular!")
        self._key = key
        self._block_size = len(key)
    def encrypt(self, message:str, add_padding = False):
        if len(message) % self._block_size != 0:
            if not add_padding:
               raise ValueError("Provided message is not in the right size")
            else:
                message += self._alphabet[0] * len(message) % self._block_size
        

class Solver(Cipher):
    """
    Mostly abstract class for Solving ciphers, usually meaning to get their key given some cipher/plaintext pairs
    """
    def __init__(self, permutation, alphabet: str = LATIN_ALPHABET):
        super().__init__(alphabet)
    def solve(self):
        """
        Somehow analytically solves the cipher for its key, given some info. 
        """
        pass
    def brute_force(self):
        """
        Prints out all possible en/decryptions of the given message
        """
        pass


class Affine_Solver(Solver):
    def __init__(self, alphabet = LATIN_ALPHABET):
        super().__init__(alphabet)

    def solve(self, pairs:list[tuple]) -> list[int]:
        """
        takes pairs (plaintext, ciphertext) and tries to find the parameters 
        """
        return self.solve_affine(pairs)
    
    def solve_affine(self, pairs:list[tuple]) -> tuple[int, int]:
        """
        takes a list of the form [(plaintext1, ciphertext1), (plaintext2, ciphertext2)] and attempts to find the key of the cipher, assuming the pairs are encoded
        with an affine cipher. 
        """
        p1, c1 = pairs[0]
        p2, c2 = pairs[1] 
        #the error here is that even though an inverse doesn't exist sometimes, there can still be a solution to the equation
        a = (self._numerise[c1]-self._numerise[c2])*pow((self._numerise[p1]-self._numerise[p2]), -1, self._alphabet_size)
        b = self._numerise[c1]-a*self._numerise[p1]
        return (a % self._alphabet_size, b % self._alphabet_size)


    def brute_force(self, message:str, decrypt = True):
        """
        Prints out all possible affine cipher decryptions (decrypt=True) or encryptions (decrypt=False) of the given ciphertext
        """
        print(self._alphabet)
        for a in range(self._alphabet_size):
            for b in range(self._alphabet_size):
                if math.gcd(a,self._alphabet_size) == 1:
                    if decrypt:
                        cipher = Affine_Cipher(a, b)
                        plaintext = cipher.decrypt(message)
                        print(f"For a={a}, b={b}, plaintext is {plaintext}")

class Caesar_Solver(Solver):
    def __init__(self, alphabet = LATIN_ALPHABET, decrypt = True):
        super().__init__()

    def brute_force(self, message: str, decrypt = False) -> str:
        if decrypt:
            for s in range(self._alphabet_size):
                cipher = Caesar_Cipher(s)
                plaintext = cipher.decrypt(message)
                print(f"For a shift of {s}, plaintext is {plaintext}")
        else:
            for s in range(self._alphabet_size):
                cipher = Caesar_Cipher(s)
                ciphertext = cipher.encrypt(message)
                print(f"For a shift of {s}, your message is encrypted as {ciphertext}")