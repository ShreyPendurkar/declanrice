p = 61
q = 53
n = p * q

phi = (p - 1) * (q - 1)
e = 17  

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

d = mod_inverse(e, phi)

print("Public Key: (", e, ",", n, ")")
print("Private Key:", d)

def encrypt(msg, e, n):
    return (msg ** e) % n

def decrypt(cipher, d, n):
    return (cipher ** d) % n

message = 300
cipher = encrypt(message, e, n)
decrypted = decrypt(cipher, d, n)

print("\nOriginal Message:", message)
print("Encrypted Message:", cipher)
print("Decrypted Message:", decrypted)