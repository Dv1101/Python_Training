List = [2000, 65, 19, 90, 20]

temp=List[0]
for count in List:
    if temp>count:
       temp = temp
    if temp<count:
       temp = count


print(temp)

"""
List.sort()
print("largest element is : ", List[-1])
"""