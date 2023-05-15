class Employee:
    empCount = 0

    def __init__(empp, name, salary):
        empp.name = name
        empp.salary = salary
        Employee.empCount+=1

    def displaycount(empp):
        print( "Name : ", empp.name , ", Salary : ", empp.salary)

    def displaycountt(empp):
        print("Total employees : ", empp.empCount)

class Transport(Employee):
    pass

p1 = Employee("Dhruv", 10000)
p2 = Employee("Lucky", 20000)

p1.displaycount()
p2.displaycount()
p2.displaycountt()

print("Employee.__doc__ : ", Employee.__doc__ )
print("Employee.__name__ : ", Employee.__name__ )
print("Employee.__module__ : ", Employee.__module__ )
print("Employee.__bases__ : ", Employee.__bases__ )
print("Employee.__dict__ : ", Employee.__dict__ )

