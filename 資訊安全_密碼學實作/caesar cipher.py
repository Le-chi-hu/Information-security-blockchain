import random
import string

charset = string.ascii_letters + string.digits + '+/'

def gen(l):
    return random.randint(0, 63)  

def enc_dec(k, plaintext, mode='enc'):
    shift = k if mode == 'enc' else -k
    return ''.join(charset[(charset.index(char) + shift) % len(charset)] for char in plaintext)

plaintext = "HELLO+world"
k = gen(1)  
ciphertext = enc_dec(k, plaintext)
decrypted_plaintext = enc_dec(k, ciphertext, mode='dec')

print("明文:", plaintext)
print("密鑰:", k)
print("密文:", ciphertext)
print("解密後的明文:", decrypted_plaintext)
