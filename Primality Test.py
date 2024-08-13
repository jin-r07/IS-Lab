def is_prime_basic(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def PrimalityTest():
    while True:
        option = input("------- Primality Test ------\nEnter the option: \n1. Check if Prime \n2. Exit\n")

        if option == "1":
            try:
                number = int(input("Enter the number to check if it's prime: "))
                result = is_prime_basic(number)
                if result:
                    print(f"{number} is a prime number.\n")
                else:
                    print(f"{number} is not a prime number.\n")
            except ValueError:
                print("Invalid input. Please enter an integer.\n")

        elif option == "2":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1 or 2.\n")


PrimalityTest()
