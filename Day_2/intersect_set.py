def intersectOfSets(arr1, arr2, arr3):
    #converting array into sets
    s1 =set(arr1)
    s2 =set(arr2)
    s3 =set(arr3)

    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)
    print(final_list)

if __name__=='__main__':
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [1,12,13,4,1,6,17,18,9,20]
    arr3 = [9,8,5,1,22,11,336,4,55,6]
    intersectOfSets(arr1,arr2,arr3)