import random
import string

def gen_key(length):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return key

def encrypt(key, plaintext):
    ciphertext = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            cipher_char = chr((ord(char) - offset + ord(key[i % len(key)]) - ord('A')) % 26 + offset)
        else:
            cipher_char = char
        ciphertext += cipher_char
    return ciphertext


def decrypt(key, ciphertext):
    plaintext = ''
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            plain_char = chr((ord(char) - offset - (ord(key[i % len(key)]) - ord('A'))) % 26 + offset)
        else:
            plain_char = char
        plaintext += plain_char
    return plaintext


key = gen_key(11)
print(f"# Gen\n{key}")

plaintext = "Hello+world"
ciphertext = encrypt(key, plaintext)
print(f"# Enc  {key} {plaintext}\n{ciphertext}")

decrypted = decrypt(key, ciphertext)
print(f"# Dec  {key} {ciphertext}\n{decrypted}")
