'''
Develop a Python script named match_case_calculator.py. 
This calculator will prompt the user to enter two numbers and 
select an operation (addition, subtraction, multiplication, or division). 
The script will then perform the selected operation using a Match Case statement and display the result.
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation =input("Choose the operation (+, -, *, /): ")

match operation:
    case x if x ==  "+":
        result = num1 + num2

    case x if x == "-":
       result = num1 - num2

    case x if x =="*":
        result = num1 * num2

    case x if x == "/":
        if num1 or num2 == 0:
            result=("sorry division by zero is not allowed")
            breakpoint
        else:
            result = num1 / num2
        

print(f"The result is {result}")


