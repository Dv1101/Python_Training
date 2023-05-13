def cave_explorer(m, n):
    
    if(m==1 or n==1):
        return 1
    return cave_explorer(m-1, n)+cave_explorer(m, n+1)


if __name__ == "__main__":
    m = int(input("Enter row no for matrix"))
    n = int(input("Enter column no for matrix"))
    print(cave_explorer(m, n))