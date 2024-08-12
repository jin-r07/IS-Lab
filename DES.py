def permute(block, table):
    return ''.join([block[i - 1] for i in table])

def shift_left(key, shift):
    return key[shift:] + key[:shift]

def xor(bits, key):
    return ''.join(['1' if bits[i] != key[i] else '0' for i in range(len(bits))])

def s_box_substitution(bits):
    sbox = [
        [0x3, 0xF, 0x0, 0x8, 0x1, 0xA, 0x4, 0xC],
        [0x5, 0x9, 0x2, 0xE, 0x6, 0xB, 0x7, 0xD]
    ]
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '04b')

def des_round(left, right, key):
    expanded_right = permute(right, [4, 1, 2, 3, 2, 3, 4, 1])
    xored = xor(expanded_right, key)
    substituted = s_box_substitution(xored[:4]) + s_box_substitution(xored[4:])
    return right, xor(left, substituted)

def des_encrypt(plain_text, key):
    initial_permutation = [2, 6, 3, 1, 4, 8, 5, 7]
    inverse_permutation = [4, 1, 3, 5, 7, 2, 8, 6]
    round_keys = [permute(shift_left(key, i), [1, 2, 3, 4, 5, 6, 7, 8]) for i in [1, 2]]

    block = permute(plain_text, initial_permutation)
    left, right = block[:4], block[4:]

    for round_key in round_keys:
        left, right = des_round(left, right, round_key)

    cipher_block = permute(right + left, inverse_permutation)
    return cipher_block

def des_decrypt(cipher_text, key):
    initial_permutation = [2, 6, 3, 1, 4, 8, 5, 7]
    inverse_permutation = [4, 1, 3, 5, 7, 2, 8, 6]
    round_keys = [permute(shift_left(key, i), [1, 2, 3, 4, 5, 6, 7, 8]) for i in [2, 1]]

    block = permute(cipher_text, initial_permutation)
    left, right = block[:4], block[4:]

    for round_key in round_keys:
        left, right = des_round(left, right, round_key)

    plain_block = permute(right + left, inverse_permutation)
    return plain_block

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))

def DES_Cipher():
    while True:
        option = input("------- DES Cipher ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option in ["1", "2"]:
            text = input("Enter the text (1 character only for simplicity): ")
            key = input("Enter an 8-bit key (e.g., 10101010): ")

            if len(text) != 1:
                print("This simple implementation only supports 1 character. Please enter a single character.\n")
                continue

            if len(key) != 8 or not all(c in '01' for c in key):
                print("Invalid key. The key must be an 8-bit binary string (e.g., 10101010).\n")
                continue

            binary_text = text_to_binary(text)
            if option == "1":
                encrypted = des_encrypt(binary_text, key)
                print(f"Encrypted Binary Text: {encrypted}\n")
            elif option == "2":
                decrypted = des_decrypt(binary_text, key)
                print(f"Decrypted Text: {binary_to_text(decrypted)}\n")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

DES_Cipher()
