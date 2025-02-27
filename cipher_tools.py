from collections import defaultdict
import math

LATIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Cipher():
    def __init__(self, alphabet:str = LATIN_ALPHABET):
        self._numerise = {}
        self._letterise = {}
        self._alphabet = alphabet
        #generate a mapping from z_n to the alphabet
        i = 0
        for c in alphabet:
            self._letterise[i] = c.lower()
            self._numerise[c.upper()] = i
            self._numerise[c.lower()] = i
            i += 1
        self._alphabet_size = len(alphabet)
class Affine_Cipher(Cipher):
    def __init__(self, a: int, b: int, alphabet:str = LATIN_ALPHABET):
        super().__init__(alphabet)
        self._a = a
        self._b = b
    
    def encrypt(self, message: str) -> str:
        encrypted = ""
        for c in message:
            encrypted += self._letterise[(self._a * self._numerise[c]+self._b) % self._alphabet_size]
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = ""
        for c in message:
            decrypted += self._letterise[((pow(self._a,-1,self._alphabet_size)) * (self._numerise[c] - self._b)) % self._alphabet_size]
        return decrypted.lower()

class Caesar_Cipher(Cipher):
    def __init__(self, shift: int, alphabet:str = LATIN_ALPHABET):
        super().__init__(alphabet)
        self._shift = shift

    def encrypt(self, message: str) -> str:
        encrypted = "" 
        for c in message:
            encrypted += self._letterise[(self._numerise[c]+ self._shift)% self._alphabet_size]
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = "" 
        for c in message:
            decrypted += self._letterise[(self._numerise[c]- self._shift) % self._alphabet_size]
        return decrypted.lower()
    
class Solver(Cipher):
    def __init__(self, alphabet: str = LATIN_ALPHABET):
        super().__init__(alphabet)
    def solve(self):
        pass
    def brute_force(self):
        pass


class Affine_Solver(Solver):
    def solve(self, pairs:list[tuple]) -> list[int]:
        """
        takes pairs (plaintext, ciphertext) and tries to find the parameters 
        """
        return self.solve_affine(pairs)
    
    def solve_affine(self, pairs:list[tuple]) -> list[int]:
        p1, c1 = pairs[0]
        p2, c2 = pairs[1]

    def brute_force(self, message:str, decrypt = False):
        """
        prints out all possible affine cipher decryptions (decrypt=True) or encryptions (decrypt=False) of the given ciphertext
        """
        print(self._alphabet)
        for a in range(self._alphabet_size):
            for b in range(self._alphabet_size):
                if math.gcd(a,self._alphabet_size) == 1:
                    if decrypt:
                        cipher = Affine_Cipher(a, b)
                        plaintext = cipher.decrypt(message)
                        print(f"For a={a}, b={b}, plaintext is {plaintext}")
