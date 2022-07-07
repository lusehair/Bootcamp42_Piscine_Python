import sys 

if len(sys.argv) == 2 :
    print("AssertionError: more than one argument are provided")

elif sys.argv[1].isnumeric() != False :
    print('AssertionError: argument is not integer')

elif int(sys.argv[1]) % 2 != 0:
    print("I'm odd")
elif int(sys.argv[1]) == 0:
    print("I'm Zero.") 
else:
    print("I'm Even.")
