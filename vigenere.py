def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    encrypted = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted += char
    return encrypted


def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted += char
    return decrypted

text = input("Enter text: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(text, key)
print("\nEncrypted Text:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)