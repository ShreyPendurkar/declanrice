def create_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    for c in key:
        if c.isalpha() and c not in matrix:
            matrix.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def process_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(c for c in text if c.isalpha())
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def encrypt_pair(pair, matrix):
    r1, c1 = find_pos(matrix, pair[0])
    r2, c2 = find_pos(matrix, pair[1])
    if r1 == r2: 
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2: 
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:  
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(pair, matrix):
    r1, c1 = find_pos(matrix, pair[0])
    r2, c2 = find_pos(matrix, pair[1])
    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair(text, key, mode='encrypt', show_matrix=False):
    matrix = create_matrix(key)
    if show_matrix:
        print("\nPlayfair Matrix:")
        for row in matrix:
            print(' '.join(row))
    pairs = process_text(text)
    result = ''
    for p in pairs:
        if mode == 'encrypt':
            result += encrypt_pair(p, matrix)
        else:
            result += decrypt_pair(p, matrix)
    return result

key = input("Enter Key: ")
plaintext = input("Enter Text: ")

cipher = playfair(plaintext, key, 'encrypt', show_matrix=True)
print("\nEncrypted:", cipher)

decrypted = playfair(cipher, key, 'decrypt', show_matrix=False)
print("Decrypted:", decrypted)
