import sys 


if len(sys.argv) < 3 :
    print("Usage: python operations.py <number1> <number2> \n Example: python operations.py 10 3\n")

input1 = sys.argv[1].lstrip('-').lstrip('+') 
input2 = sys.argv[2].lstrip('-').lstrip('+')

if input1.isnumeric() == False or input2.isnumeric() == False:
    print("AssertionError: only numbers")

elif len(sys.argv) > 3  :
    print("AssertionError: Too many arguments") 

 


else :

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("Sum: ".ljust(10), num1 + num2)
    print("Difference: ".ljust(10), abs(num1-num2)) 
    print("Product: ".ljust(10), num1 * num2)
    if num1 == 0 or num2 == 0 :
        print("Quotient: ".ljust(10)  + "ERROR (div by zero)")
    else :
        print("Quotient: ".ljust(10) + "{:.2f}".format(float(num1 / num2)))
    if num1 == 0 or num2 == 0 :
        print("Remainder: ".ljust(10) + "ERROR (modulo by zero)")
    else :
        print("Remainder: ".ljust(10), num1%num2)
