A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

B = [[5, 10, 15, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

ans = [[0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   

print("3rd column =", column)

for i in range(len(A)):
    for j in range(len(A[0])):
       ans[i][j] = A[i][j] + B[i][j]

print("\n The matrix A  : \n")
print("A =", A) 
print("\n The matrix B  : \n")
print("B =", B) 
print("\n The adition of matrix A & B is : \n")
print(ans)

for i in range(len(A)):
    for j in range(len(A[0])):
       ans[i][j] = A[i][j] * B[i][j]

print("\n The multiplication of matrix A & B is : \n")
print(ans)

for i in range(len(A)):
    for j in range(len(A[0])):
       ans[i][j] = A[i][j] - B[i][j]

print("\n The substraction of matrix A & B is : \n")
print(ans)

