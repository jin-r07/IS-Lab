def CaesarCipher():
    while True:
        option = input("------- Caesar Cipher ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")
        encoded_text = ""
        decoded_text = ""

        if option == "1":
            plain_text = input("Plain text: ")
            shift = int(input("Enter the shift number: "))
            for char in plain_text:
                if char.isalpha():
                    shifted = ord(char) + shift
                    if char.islower():
                        if shifted > ord('z'):
                            shifted -= 26
                        encoded_text += chr(shifted)
                    elif char.isupper():
                        if shifted > ord('Z'):
                            shifted -= 26
                        encoded_text += chr(shifted)
                else:
                    encoded_text += char
            print(f"Encoded Text: {encoded_text}\n")

        elif option == "2":
            encoded_text = input("Encrypted text: ")
            shift = int(input("Enter the shift number: "))
            for char in encoded_text:
                if char.isalpha():
                    shifted = ord(char) - shift
                    if char.islower():
                        if shifted < ord('a'):
                            shifted += 26
                        decoded_text += chr(shifted)
                    elif char.isupper():
                        if shifted < ord('A'):
                            shifted += 26
                        decoded_text += chr(shifted)
                else:
                    decoded_text += char
            print(f"Decoded Text: {decoded_text}\n")

        elif option == "3":
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

CaesarCipher()