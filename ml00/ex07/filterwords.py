import sys

array = sys.argv[1]

print(int(sys.argv[2]))

for x in array :
    if len(x) <= int(sys.argv[2]) :
        array.remove(x)

print(array)