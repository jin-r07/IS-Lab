def encrypt_rail_fence(plain_text, rails):
    if rails == 1:
        return plain_text

    rail_pattern = [''] * rails
    row, direction = 0, 1

    for char in plain_text:
        rail_pattern[row] += char
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return ''.join(rail_pattern)

def decrypt_rail_fence(cipher_text, rails):
    if rails == 1:
        return cipher_text

    rail_lengths = [0] * rails
    row, direction = 0, 1

    for char in cipher_text:
        rail_lengths[row] += 1
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    rail_pattern = [''] * rails
    index = 0

    for i in range(rails):
        rail_pattern[i] = cipher_text[index:index + rail_lengths[i]]
        index += rail_lengths[i]

    decrypted_text = []
    row, direction = 0, 1

    for i in range(len(cipher_text)):
        decrypted_text.append(rail_pattern[row][0])
        rail_pattern[row] = rail_pattern[row][1:]
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return ''.join(decrypted_text)

def RailFenceCipher():
    while True:
        option = input("------- Rail Fence Cipher ------\nEnter the option: \n1. Encrypt \n2. Decrypt \n3. Exit.\n")

        if option in ["1", "2"]:
            text = input("Enter the text: ")
            try:
                rails = int(input("Enter the number depth: "))
                if rails <= 0:
                    print("Number of rails should be a positive integer.\n")
                    continue
            except ValueError:
                print("Invalid input for rails. Please enter an integer.\n")
                continue

            if option == "1":
                result = encrypt_rail_fence(text, rails)
                print(f"Encoded Text: {result}\n")
            elif option == "2":
                result = decrypt_rail_fence(text, rails)
                print(f"Decoded Text: {result}\n")

        elif option == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

RailFenceCipher()
