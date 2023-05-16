def segregating(array, x) :
# Counting the 0's in array
   count = 0
   for i in range(0, x) :
      if (array[i] == 0) :
         count = count + 1


   for i in range(0, count) :
      array[i] = 0


   for i in range(count, x) :
      array[i] = 1


def print_the_array(array , x) :
   print( "The segregated array is :",end = "")

   for i in range(0, x) :
      print(array[i] , end = " ")


array = [0,1,1,0,0,1,0,0,0]
x = len(array)

segregating(array, x)
print_the_array(array, x)

