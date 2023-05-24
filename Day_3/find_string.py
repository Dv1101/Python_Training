import re

str = "Python is easy to learn"
print("\n The original string is : " +str)

word = "easy"

str = str.split()
res=-1

for idx in str:
    if len(re.findall(word, idx) > 0):
        res = str.index(idx) + 1

print("The location of word is : " +str(res))
