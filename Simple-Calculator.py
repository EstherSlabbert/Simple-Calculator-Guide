# ============================
# Simple Functional Calculator
# ============================

# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# function to divide two numbers
def divide(num1, num2):
    return num1 / num2


# function to use modulo on two numbers (%)
def modulo(num1, num2):
    return num1 % num2


# Output to tell the user the function of the program.
print("This is a simple calculator program.\nIt takes 2 numbers and performs calculations.")

# Verifies correct user input by continuing to ask for correct input until it is provided
while True:
    # try/except verifies correct input type
    try:
        # gets user input to choose which function to perform and provides choices
        choice = int(input("""\
Enter your choice of calculation with an integer referencing the list below:
1 for addition
2 for subtraction
3 for multiplication
4 for division
5 for modulus
Operation choice as an integer:
"""))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# once the input is valid the program continues from here based on the user's choice
if choice in (1, 2, 3, 4, 5):
    # Verifies correct input type - keeps asking until correct
    while True:
        # try/except verifies correct input type
        try:
            # gets 2 numbers to perform the selected function on
            num1 = float(input("\n Enter your first number: "))
            num2 = float(input("\n Enter your second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
else:
    print("Invalid option. Try running the program again.")

# performs the function based on the input received
if choice == 1:
    # returns added numbers
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    # returns subtracted numbers
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    # returns multiplied numbers
    print(num1, "x", num2, "=", multiply(num1, num2))

elif choice == 4:
    # returns divided numbers
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == 5:
    # returns modulus (i.e. the remainder of num1/num2)
    print(num1, "%", num2, "=", modulo(num1, num2))
