import math


def gcd(a, b):
    return math.gcd(a, b)


def EuclideanAlgorithm():
    while True:
        option = input("------- Euclidean Algorithm ------\nEnter the option: \n1. Find GCD \n2. Exit.\n")

        if option == "1":
            try:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
            except ValueError:
                print("Invalid input.\n")
                continue

            result = gcd(a, b)
            print(f"The GCD of {a} and {b} is {result}\n")

        elif option == "2":
            print("Exiting")
            break

        else:
            print("Invalid option.\n")


EuclideanAlgorithm()
