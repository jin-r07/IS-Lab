from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


def generate_rsa_keys():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    # Generate public key
    public_key = private_key.public_key()

    return private_key, public_key


def serialize_private_key(private_key):
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )


def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


def rsa_encrypt(public_key, plaintext):
    encrypted = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted


def rsa_decrypt(private_key, encrypted):
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()


def RSAExample():
    private_key, public_key = generate_rsa_keys()

    print("RSA Keys Generated.\n")

    while True:
        option = input(
            "------- RSA ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option == "1":
            plaintext = input("Enter the text to encrypt: ")
            encrypted = rsa_encrypt(public_key, plaintext)
            print(f"Encrypted Text (hex): {encrypted.hex()}\n")

        elif option == "2":
            encrypted_text_hex = input("Enter the encrypted text (hex): ")
            encrypted = bytes.fromhex(encrypted_text_hex)
            decrypted = rsa_decrypt(private_key, encrypted)
            print(f"Decrypted Text: {decrypted}\n")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")


RSAExample()
