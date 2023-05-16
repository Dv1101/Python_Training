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



x = int(input("Enter value a : "))
y = int(input("Enter value b :"))

sum = add(x, y)
print(sum)
sum = addd(x, y)
print(sum)
