def shorting(n,office,array):
    min_weight = min(array)
    max_weight = max(array)
    office_weight = array[office]
    min_index= array.index(min_weight)
    max_index= array.index(max_weight)
    effort = effort1 = 0
    if max_weight != office:
        effort1 = min_weight * office_weight
        array[min_index],array[office] = array[office], array[min_index]
        office_weight = array[office]    
    effort2 =  (office_weight * max_weight)
    effort = effort1 +effort2   
    array[office],array[max_index] = array[max_index],array[office]
    print("Office Loaction is :",office)
    print("MAximium weigth parcel is :",max_weight)
    print("office  and weight are now on same place :")
    print(array)
    print("Efffot:",effort)

paecel=[]
n = int(input("Enter the number of parcel :"))
for i in range(n):
    print("Enter weight for ",i,"parcel")
    weight = int(input())
    paecel.append(weight)
print("Your list of parcel is : ")
print(paecel)
office_location = int(input("Enter oflice location :"))
shorting(n,office_location-1,paecel)