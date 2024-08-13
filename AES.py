from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext.hex()


def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(bytes.fromhex(ciphertext))
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    return decrypted_text.decode()


def AESExample():
    while True:
        option = input("------- AES Encryption ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option in ["1", "2"]:
            text = input("Enter the text : ")
            key = input("Enter the 16/24/32-byte key: ").encode()

            if len(key) not in [16, 24, 32]:
                print("Key must be 16, 24, or 32 bytes long.\n")
                continue

            if option == "1":
                result = aes_encrypt(text, key)
                print(f"Encrypted Text: {result}\n")
            elif option == "2":
                result = aes_decrypt(text, key)
                print(f"Decrypted Text: {result}\n")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")


AESExample()
