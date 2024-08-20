def is_prime(n):
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
        option = input("------- Primality Test ------\nEnter the option: \n1. Check if Prime \n2. Exit.\n")

        if option == "1":
            try:
                number = int(input("Enter a number: "))
                result = is_prime(number)
                if result:
                    print(f"{number} is prime.\n")
                else:
                    print(f"{number} is not prime.\n")
            except ValueError:
                print("Invalid input.\n")

        elif option == "2":
            print("Exiting")
            break

        else:
            print("Invalid option.\n")


PrimalityTest()
