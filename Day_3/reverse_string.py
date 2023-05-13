str = "Hello world !! Vasu"

s = str.split()[::-1]
l =[]
for i in s:
   l.append(i)
   
print(" ".join(l))
print(str[::-1])