def consecutive(binary):
    count=0
    result=0

    for i in range(len(binary)-1):
        if(binary[i]==0):
            count=0
        else:
            count+=1
            result = max(result, count)
    return result
            



if __name__=="__main__":
    binary = list(map(int, input("Enter 0 or 1 : ").split(" ")))
    print(consecutive(binary))