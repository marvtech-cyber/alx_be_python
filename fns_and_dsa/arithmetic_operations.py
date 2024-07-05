'''
Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations.
 This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

Requirements for arithmetic_operations.py:
Function Definition:
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values:
 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py scrip
t can recognize and display appropriately.
Return the result of the arithmetic operation.
'''

def perform_operation( num1, num2, operation):
    match operation:
        case x if x == 'add':
            return num1 + num2
        
        case x if x == 'subtract':
            return num1 - num2
        
        case x if x == 'multiply':
            return num1 * num2
        
        case 'division':
            if num1 or num2 == 0:
                return "Division by zero not allowed"
            else:
                return num1 // num2
