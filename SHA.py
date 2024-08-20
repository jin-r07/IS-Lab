import hashlib

def sha256_hash(text):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the bytes of the text
    sha256.update(text.encode())
    # Return the hexadecimal digest of the hash
    return sha256.hexdigest()

def sha256_example():
    text = input("Enter the text: ")
    hash_value = sha256_hash(text)
    print(f"SHA-256 Hash: {hash_value}")

sha256_example()
