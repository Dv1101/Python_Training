from collections import OrderedDict

def removeDupWithoutOrder(str):
    return "".join(set(str))

def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__=="__main__":
    str="DhruvDhruvDhruvvvvvvvuuuuupythonpython"
    print(removeDupWithoutOrder(str))
    print(removeDupWithOrder(str))
