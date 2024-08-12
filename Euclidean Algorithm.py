def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    while True:
        option = input("------- Euclidean Algorithm ------\nEnter the option: \n1. Find GCD \n2. Exit\n")

        if option == "1":
            try:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                gcd = euclidean(a, b)
                print(f"The GCD of {a} and {b} is {gcd}\n")
            except ValueError:
                print("Invalid input. Please enter integers.\n")

        elif option == "2":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1 or 2.\n")

if __name__ == "__main__":
    main()
