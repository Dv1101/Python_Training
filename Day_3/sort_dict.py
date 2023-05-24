list = [{"Name":"Dhruv", "Age":20},
        {"Name":"Vishal", "Age":22},
        {"Name":"Vasu", "Age":2},
        {"Name":"Deep", "Age":99},
        {"Name":"JAyraj", "Age":30},
        {"Name":"Neha", "Age":10},
        {"Name":"Radhika", "Age":20}]
print("\n")
print("\n")
print(list)
print("\n")
print("The list printed sorting by age : ")
print("\n")
print(sorted(list, key=lambda i: i["Age"]))
print("\n")
print("The list printed sorting by Name and Age : ")
print("\n")
print(sorted(list, key=lambda i: (i["Age"], i["Name"])))
print("\n")
print("The list printed sorting by age in reverse order : ")
print("\n")
print(sorted(list, key=lambda i: i["Age"], reverse=True))