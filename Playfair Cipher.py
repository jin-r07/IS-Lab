def create_matrix(key):
    key = "".join(sorted(set(key.upper().replace('J', 'I')), key=key.index))
    key += "".join([c for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if c not in key])
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    i, prepared = 0, ""
    while i < len(text):
        prepared += text[i] + ('X' if i == len(text) - 1 or text[i] == text[i + 1] else text[i + 1])
        i += 1 if i == len(text) - 1 or text[i] == text[i + 1] else 2
    return prepared

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def transform(text, matrix, encrypt=True):
    transformed = ""
    shift = 1 if encrypt else -1
    for i in range(0, len(text), 2):
        r1, c1 = find_position(text[i], matrix)
        r2, c2 = find_position(text[i + 1], matrix)
        if r1 == r2:
            transformed += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            transformed += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else:
            transformed += matrix[r1][c2] + matrix[r2][c1]
    return transformed

def PlayfairCipher():
    while True:
        option = input("------- Playfair Cipher ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")
        if option in {"1", "2"}:
            key = input("Enter keyword: ").replace(" ", "")
            text = input("Enter text: ").replace(" ", "")
            matrix = create_matrix(key)
            result = transform(prepare_text(text), matrix, encrypt=(option == "1"))
            print(f"Result: {result}\n")
        elif option == "3":
            break
        else:
            print("Invalid option")

PlayfairCipher()
