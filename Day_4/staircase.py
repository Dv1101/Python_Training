"""Staircase problem"""
"""There are n stairs, a person standing at the bottom wants to reach the top. the person can climb either 1 or 2 stairs at a  time. count the number of ways, person can reach the top"""


# A program to count the number of ways
# to reach n'th stair
 
# Recursive function used by countWays
def countWaysUtil(n, m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<= m and i<= n:
        res = res + countWaysUtil(n-i, m)
        i = i + 1
    return res
     
# Returns number of ways to reach s'th stair   
def countWays(s, m):
    return countWaysUtil(s + 1, m)
     
 
# Driver program
s, m = 4, 2
print("Number of ways =", countWays(s, m))