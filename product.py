import math

def caesar_encrypt(text):
    text = text.upper().replace(" ", "")
    return "".join(chr((ord(c) - 65 + 3) % 26 + 65) for c in text)

def caesar_decrypt(text):
    return "".join(chr((ord(c) - 65 - 3) % 26 + 65) for c in text)

def transpose_encrypt(text, cols=3):
    rows = math.ceil(len(text) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                matrix[r][c] = text[index]
                index += 1

    return ''.join(matrix[r][c] for c in range(cols) for r in range(rows) if matrix[r][c])

def transpose_decrypt(text, cols=3):
    rows = math.ceil(len(text) / cols)
    full_cols = len(text) % cols
    if full_cols == 0:
        full_cols = cols

    col_lengths = [rows if c < full_cols else rows - 1 for c in range(cols)]
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for c in range(cols):
        for r in range(col_lengths[c]):
            matrix[r][c] = text[index]
            index += 1

    return ''.join(matrix[r][c] for r in range(rows) for c in range(cols) if matrix[r][c])

plaintext = input("Enter plaintext: ").upper().replace(" ", "")
caesar_text = caesar_encrypt(plaintext)
print("\nAfter Caesar Cipher:", caesar_text)

encrypted = transpose_encrypt(caesar_text)
print("Final Encrypted Text:", encrypted)

decrypted_step1 = transpose_decrypt(encrypted)
final_text = caesar_decrypt(decrypted_step1)
print("Decrypted Text:", final_text)