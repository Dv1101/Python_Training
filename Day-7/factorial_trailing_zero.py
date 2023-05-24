def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number for factorial : "))
facto = factorial(n)
print("Factorial is : ", facto)


facto = str(facto)

count=0
result=0

for i in range(len(facto)):
        if (facto[i] != "0"):
            count = 0
        else:
            count+= 1
            result = max(result, count)

    
print("Number of zero in factorial is : " , result)