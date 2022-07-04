import sys 


assert len(sys.argv) == 2, 'more than one argument is provided' 
assert sys.argv[1].isnumeric() != False, 'argument is not integer'

if int(sys.argv[1]) % 2 != 0:
    print("I'm odd")
elif int(sys.argv[1]) == 0:
    print("I'm Zero.") 
else:
    print("I'm Even.")
