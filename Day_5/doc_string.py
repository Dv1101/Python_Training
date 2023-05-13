def oddEven(x):
    """Fuction to check whether number is even or not
    
       Args:
        x (int): Numeric value

    Returns:
        Print function"""
    
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

    print(oddEven.__doc__)

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    oddEven(x)