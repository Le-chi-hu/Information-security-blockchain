import hashlib
import numpy as np
import string
import random

charset = string.ascii_letters + string.digits + '+/'

def pseudo_random_function(key, iv, n):
    input_bytes = (str(key) + str(iv)).encode('utf-8')
    hash_object = hashlib.sha256(input_bytes)
    hex_dig = hash_object.hexdigest()
    int_dig = int(hex_dig, 16)
    np.random.seed(int_dig % (2**32 - 1))
    return np.random.randint(0, len(charset), n)

def Gen(l):
    key = ''.join(np.random.choice(list(charset), l))
    return key

def Enc(l, n, key, m):
    iv_len = max(l + 5, n + 5)
    iv = ''.join(random.choices(charset, k=iv_len))
    k_tilde = pseudo_random_function(key, iv, n)
    c = (m + k_tilde) % len(charset)
    ciphertext_ascii = ''.join(charset[i] for i in c)
    ciphertext_with_key = key + ciphertext_ascii
    return iv, ciphertext_with_key

def Dec(l, n, key, iv, c):
    k_tilde = pseudo_random_function(key, iv, n)
    c_int = np.array([charset.index(ch) for ch in c[5:]])
    m = (c_int - k_tilde) % len(charset)
    decrypted_text = ''.join(charset[i] for i in m)
    return decrypted_text

plaintext = np.array([charset.index(c) for c in 'Hello+world'])
key = Gen(5)
iv, ciphertext_with_key = Enc(len(plaintext), len(plaintext), key, plaintext)
decrypted_text = Dec(len(plaintext), len(ciphertext_with_key)-5, key, iv, ciphertext_with_key)

print(f"Key: {key}")
print(f"Plaintext: {'Hello+world'}")
print(f"Ciphertext: {ciphertext_with_key}") 
print(f"Decrypted text: {decrypted_text}")
