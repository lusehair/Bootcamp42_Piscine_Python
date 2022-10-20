import sys 

  




if len(sys.argv) > 1 :

    if len(sys.argv) != 2 :
        print("AssertionError: more than one argument are provided")
        exit()

    num = sys.argv[1]; 

    if(num.find('-') != -1) : 
        num = num.lstrip('-')
    if(num.find('+') != -1) :
        num = num.lstrip('+')
    if num.isnumeric() == False :
        print('AssertionError: argument is not integer')

    elif int(num)% 2 != 0:
        print("I'm odd")
    elif int(num) == 0:
        print("I'm Zero.") 
    else:
        print("I'm Even.")
