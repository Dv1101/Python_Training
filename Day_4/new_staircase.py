def findstep(n):
    if (n==1 or n==0):
        return 1
    elif(n==2):
        return 2
    else:
        return findstep(n-2)+findstep(n-1)

# Driver program
s, m = 4, 2
n=4
print("Number of ways =", findstep(n))