import sys

if len(sys.argv) != 3:
    print("ERROR")

elif sys.argv[2].isdigit() == False:
    print("ERROR")

else :
    array = sys.argv[1].split() 
    ret =[]
    for x in array :
        if len(x) > int(sys.argv[2]) :
            ret.append(x)        
    print(ret)