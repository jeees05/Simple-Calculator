#Simple Calculator

def calculator():
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Pick (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero! Try another number")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice, try again!")

if __name__ == "__main__":
    calculator()
