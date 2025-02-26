from collections import defaultdict

#assumption: alphabet is lowercase english alphabet. How can this be generalised?

class Cipher():
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
            encrypted += self.z26_to_letter(self.letter_to_z26(c)+ self._shift)
        return encrypted.upper()

    def decrypt(self, message: str) -> str:
        decrypted = "" 
        for c in message:
            decrypted += self.z26_to_letter(self.letter_to_z26(c)- self._shift) 
        return decrypted.lower()