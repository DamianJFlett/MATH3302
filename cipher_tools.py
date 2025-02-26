from collections import defaultdict
#add to general tools
def letter_to_z26(letter:str):
    return ord(letter.lower()) - 97
def z26_to_letter(number:int):
    return chr(number+97)

#assumption: alphabet is lowercase english alphabet. How can this be generalised?

def apply_affine_cipher(message:str,  a:int, b:int) -> str:
    encrypted = ""
    for c in message:
        encrypted += z26_to_letter((a * letter_to_z26(c)+b) % 26)
    return encrypted.upper()
def apply_inverse_affine_cipher(message:str, a:int, b:int) -> str:
    decrypted = ""
    for c in message:
        decrypted += z26_to_letter(((pow(a,-1,26)) * (letter_to_z26(c) - b)) % 26)
    return decrypted.lower()