# How to make a simple calculator in Python
###### by Esther Slabbert

#### Please note that this is a guide for a simple calculator, which can be used as a template and modified to the creator's preferences. Feel free to add comments to make your code more readable.

1. Create a new .py file and name it appropriately.
2. Open the .py file that you have created.
3. Start your code by defining several functions for the different operations you would like to include in your calculator for operations between two numbers. (Note: You may wish to alter which functions you would like to make/include and how you would like to make them. Below is only an example of how your code could look.)
    <ul>
      <li>Define a function for addition</li>
      To do this, type the following in your python file:
      <pre>def add(num1, num2):
       return num1 + num2</pre>
      <li>Define a function for subtraction</li>
      To do this, type the following in your python file:
      <pre>def subtract(num1, num2):
       return num1 - num2</pre>
      <li>Define a function for multiplication</li>
      To do this, type the following in your python file:
      <pre>def multiply(num1, num2):
       return num1 * num2</pre>
      <li>Define a function for division</li>
      To do this, type the following in your python file:
      <pre>def divide(num1, num2):
       return num1 / num2</pre>
      <li>Define a function for modulo</li>
      To do this, type the following in your python file:
      <pre>def modulo(num1, num2):
       return num1 % num2</pre>
    </ul>
4. Next you should get some input from the user to choose what operation they would like to perform. To do this, type the following (or similar) in your python file:
    <ul>
        <pre>choice = int(input("""\
    Enter your choice of calculation with an integer referencing the list below:
    1 for addition
    2 for subtraction
    3 for multiplication
    4 for division
    5 for modulus
    Operation choice as an integer:
    """))</pre>
    </ul>
5. Next we need the two numbers that the user wishes to use the operation on. To ensure the user input a valid option for the operations provided, we need to code this into an if statement. To do this, type the following (or similar) in your python file:
    <ul>
        <pre>if choice in (1, 2, 3, 4, 5):
       num1 = float(input("\n Enter your first number: "))
       num2 = float(input("\n Enter your second number: "))
   else:
       print("Invalid option. Try running the program again.")</pre>
    </ul>
6. Next we need to take the information the user input and put it into action. So we need to create several if statements containing the functions we defined in step 3 to determine which operation will be performed. Then we need to input the two numbers that the user wants the operations to be performed on in these functions and print the results as something readable to the user. To do this, type the following (or similar) in your python file:
    <ul>
        <pre>if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
    print(num1, "x", num2, "=", multiply(num1, num2))

    elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 5:
    print(num1, "%", num2, "=", modulo(num1, num2))</pre>
    </ul>
7. Now you can run your program and try it out.
8. Congratulations! Now you have successfully created a simple calculator in Python, which you can improve upon and play around with.

(Comments can be made by using '#' before writing your comment or notes in Python.)
