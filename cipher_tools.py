from collections import defaultdict
import math
class Cipher():
    """
    preconditions:alphabet is lowercase english alphabet.
    """
    #may generalise the above in some way later
    def __init__(self):
        pass
    def letter_to_z26(self, letter:str):
        return ord(letter.lower()) - 97

    def z26_to_letter(self, number:int):
        return chr(number+97)

class Affine_Cipher(Cipher):
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b
    
    def encrypt(self, message: str) -> str:
        encrypted = ""
        for c in message:
            encrypted += self.z26_to_letter((self._a * self.letter_to_z26(c)+self._b) % 26)
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = ""
        for c in message:
            decrypted += self.z26_to_letter(((pow(self._a,-1,26)) * (self.letter_to_z26(c) - self._b)) % 26)
        return decrypted.lower()

class Caesar_Cipher(Cipher):
    def __init__(self, shift: int):
        self._shift = shift

    def encrypt(self, message: str) -> str:
        encrypted = "" 
        for c in message:
            encrypted += self.z26_to_letter((self.letter_to_z26(c)+ self._shift)% 26)
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = "" 
        for c in message:
            decrypted += self.z26_to_letter((self.letter_to_z26(c)- self._shift) % 26) 
        return decrypted.lower()
    
class Solver():
    def __init__(self, type:str):
        self._type = type

    def solve(self, pairs:list[tuple]) -> list[int]:
        """
        takes pairs (plaintext, ciphertext) and tries to find the parameters 
        """
        if self._type == "Affine":
            return self.solve_affine(pairs)
    
    def solve_affine(self, pairs:list[tuple]) -> list[int]:
        p1, c1 = pairs[0]
        p2, c2 = pairs[1]

    def brute_force(self, message: str,decrypt = False):
        if self._type == "Affine":
            self.brute_force_affine(message, decrypt)

    def brute_force_affine(self, message:str, decrypt = False):
        """
        prints out all possible affine cipher decryptions (decrypt=True) or encryptions (decrypt=False) of the given ciphertext
        """
        for a in range(26):
            for b in range(26):
                if math.gcd(a,26) == 1:
                    if decrypt:
                        cipher = Affine_Cipher(a, b)
                        plaintext = cipher.decrypt(message)
                        print(f"For a={a}, b={b}, plaintext is {plaintext}")
                    else:
                        pass
