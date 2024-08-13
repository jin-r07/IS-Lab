from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext.hex()


def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(bytes.fromhex(ciphertext))
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()


def DESExample():
    while True:
        option = input("------- DES Encryption ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option in ["1", "2"]:
            text = input("Enter the text: ")
            key = input("Enter the 8-byte key: ").encode()

            if len(key) != 8:
                print("Key must be 8 bytes long.\n")
                continue

            if option == "1":
                result = des_encrypt(text, key)
                print(f"Encrypted Text: {result}\n")
            elif option == "2":
                result = des_decrypt(text, key)
                print(f"Decrypted Text: {result}\n")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")


DESExample()
