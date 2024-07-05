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
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        if num1 or num2:
            return "division by zero not posible"
        return num1 // num2
        
