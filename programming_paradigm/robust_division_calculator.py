def safe_divide(numerator, denominator):
    try:
       numerator = float(numerator)
       denominator = float(denominator)
    except ValueError:
        return f"Error: Please enter numeric values only."
    try:
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
            return ZeroDivisionError("Error: Cannot divide by zero.")

    
