def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift

    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result


def CaesarCipher():
    while True:
        option = input("------- Caesar Cipher ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option in ["1", "2"]:
            text = input("Enter the text: ")
            try:
                shift = int(input("Enter the shift number: "))
            except ValueError:
                print("Invalid input for shift.\n")
                continue

            if option == "1":
                result = caesar_cipher(text, shift, encrypt=True)
                print(f"Encoded Text: {result}\n")
            elif option == "2":
                result = caesar_cipher(text, shift, encrypt=False)
                print(f"Decoded Text: {result}\n")

        elif option == "3":
            print("Exiting")
            break

        else:
            print("Invalid option.\n")


CaesarCipher()
