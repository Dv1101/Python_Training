'''
"""SWAP BY INDEX"""
a_list = ["a", "b", "c"]
a_list[0], a_list[2] = a_list[2], a_list[0]

print(a_list)

"""SWAP BY VALUE"""
a_list = ["a", "b", "c","d","e"]

index1 = a_list.index("a")
index2 = a_list.index("e")
a_list[index1], a_list[index2] = a_list[index2], a_list[index1]

print(a_list)
'''
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], [pos1]
    return list

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))