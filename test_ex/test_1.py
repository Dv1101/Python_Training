def hurdlerace(k, height):
    portion = 0

    for i in range (max(height)):
        if max(height)- k >0:
            k+=1
            portion+=1
    return portion

if __name__ == "__main__":
    k = int(input("Enter height of a character can jump : "))

    heights = list(map(int, input("Enter heights : ").split(" ")))
    print("Total portion is used : ", hurdlerace(k, heights))