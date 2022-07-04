import sys 

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if len(sys.argv) > 2  :
    print("InputError: Too many arguments") 
    print("Usage: python operations.py <number1> <number2> \n Example: python operations.py 10 3\n")

if sys.argv[1].isalnum() == False or sys.argv[2].isalnum == False or sys.argv[1].count('.') or  sys.argv[2].count('.'):
    print("InputError: only numbers") 
    print("Usage: python operations.py <number1> <number2> \n Example: python operations.py 10 3\n")

if len(sys.argv) < 2 :
    print("Usage: python operations.py <number1> <number2> \n Example: python operations.py 10 3\n")

print("Sum: ".ljust(10), num1 + num2)
print("Difference: ".ljust(10), abs(num1-num2)) 
print("Product: ".ljust(10), num1 * num2)
if num1 == 0 or num2 == 0 :
    print("Quotient: ".ljust(10)  + "ERROR (div by zero)")
else :
    print("Quotient: ".ljust(10), num1//num2)
if num1 == 0 or num2 == 0 :
    print("Remainder: ".ljust(10) + "ERROR (modulo by zero)")
else :
    print("Remainder: ".ljust(10), num1%num2)
