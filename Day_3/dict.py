import sys

dict = {1:"Dhruv", 2:"Vasu", 3:"Lucky"}
dict3 = {4:"Vishal", 5:"Deep",6:"Tirth", 7:"Malav"}
print(dict)
print(dict[3])
print(dict.keys)
print(dict.keys())
print(dict.values)
print(dict.values())
print("length of this dictionary is : ",len(dict))
print("Size of this dictionary is : ",str(sys.getsizeof(dict)))

def Merge(dict, dict3):
    return(dict.update(dict3))

print(Merge(dict,dict3))
print(dict)

