def add(x, y):
    carry = 0
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

def addd(x, y):
    ans  = (x-(~y)-1)
    return ans
""" a=2 b=3
    c = (a-(~b)-1)
      = a -(-1-b) -1
      = 2 -(-1-3) -1
      = 2 -(-4) -1
      = 2+4 -1
      = 6 -1
      = 5
"""



x = int(input("Enter value a : "))
y = int(input("Enter value b :"))

sum = add(x, y)
print(sum)
sum = addd(x, y)
print(sum)
