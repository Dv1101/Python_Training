a = list(map(int, input("Enter arr A : ").split(" ")))
b = list(map(int, input("Enter arr B : ").split(" ")))

min_a = min(a)
a = sorted(a)
b = sorted(b, reverse = True)

print(a)
print(b)
s = 0
for i in range (len(b)):
    s = s + (a[i] * b[i])

print("Minimum Value is : ", s)
