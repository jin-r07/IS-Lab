def PlayfairCipher():
    while True:
        option = input("Enter option: \n1. Encrypt\n2. Decrypt\n3. Exit")
        if option == "1":
            print("Option 1")
        elif option == "2":
            print("Option 2")
        elif option == "3":
            break
        else:
            print("Invalid option")


PlayfairCipher()