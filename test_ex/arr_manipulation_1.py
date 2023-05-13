def mineffort(n, k, items):
    minitem = min(items)
    maxitem = max(items)
    minitemind = items.index(minitem)
    maxitemind = items.index(maxitem)

    '''print(minitemind)
    print(maxitemind)'''
    effort = minitem * items[k-1]
    swap(minitemind, k-1)

    effort+= maxitem * items[k-1]
    swap(maxitemind, k-1)

    minitemind = items.index(minitem)
    effort+= minitem * items[0]
    swap(minitemind, 0)
    return effort

def swap(a, b):
    temp = items[a]
    items[a] = items[b]
    items[b] = temp

if __name__ == "__main__":
    items = [20, 50, 30, 80, 70]  
    n=len(items)
    print(items)
    k=int(input("Enter master's ofice location"))
    print(mineffort(n,k,items))


