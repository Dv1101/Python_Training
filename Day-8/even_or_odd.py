"""even or odd without modulous"""

def evenodd(n):

    if n & 1 == 0:
        return "even"
    else:
        return "odd"
        

n = int(input("Enter a number to check its odd or even"))

print(evenodd(n))

