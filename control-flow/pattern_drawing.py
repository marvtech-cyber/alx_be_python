'''
Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer,
 then use nested loops to print a square pattern of that size made of asterisks (*).
'''
pattern_size = int(input("Enter the size of the pattern: "))

i = 0


while i < pattern_size:
    j = 0
    while j < pattern_size:
        print("*", end=" ")
        j+=1
    print()
    i+=1
