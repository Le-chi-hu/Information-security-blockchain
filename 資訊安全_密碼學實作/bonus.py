import hashlib
import numpy as np

def pseudo_random_function(key, iv, n):
    input_bytes = (str(key) + str(iv)).encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    hex_dig = hash_object.hexdigest()
    int_dig = int(hex_dig, 16)
    np.random.seed(int_dig % (2**32 - 1))
    return np.random.randint(0, 256, n)

def Gen(l):
    return np.random.randint(0, 256, l)

def Enc(l, n, key, m):
    iv = np.random.randint(0, 256, l)
    k_tilde = pseudo_random_function(key, iv, n)
    c = (m + k_tilde) % 256  
    return iv, c

def Dec(l, n, key, iv, c):
    k_tilde = pseudo_random_function(key, iv, n)
    m = (c - k_tilde) % 256  
    return m


plaintext = np.array([0b01010100, 0b01110010, 0b01110101, 0b01110100, 0b01101000], dtype=np.uint8)
key = Gen(10)
iv, ciphertext = Enc(10, len(plaintext), key, plaintext)
decrypted = Dec(10, len(ciphertext), key, iv, ciphertext)

print(f"Key : {' '.join(f'{x:08b}' for x in key)}")
print(f"Plaintext : {' '.join(f'{x:08b}' for x in plaintext)}")
print(f"Ciphertext : {' '.join(f'{x:08b}' for x in ciphertext)}")
print(f"Decrypted text : {' '.join(f'{x:08b}' for x in decrypted)}")
