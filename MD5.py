import hashlib

def md5_hash(text):
    # Create an MD5 hash object
    md5 = hashlib.md5()
    # Update the hash object with the bytes of the text
    md5.update(text.encode())
    # Return the hexadecimal digest of the hash
    return md5.hexdigest()

def md5_example():
    text = input("Enter the text: ")
    hash_value = md5_hash(text)
    print(f"MD5 Hash: {hash_value}")

md5_example()
