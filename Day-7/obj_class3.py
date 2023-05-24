class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " , self.name ," and i'm : ", self.age ," old.")

p1 = Person("John", 36)
p2 = Person("Neha", 46)
p3 = Person("Dhruv", 20)
p4 = Person("Vasu", 20)
p1.myfunc()
p2.myfunc()
p3.myfunc()
p4.myfunc()

'''
object (real time entity)
class (collection of objects)
inheritance(parent - class pbject properties)
polymorphism (many forms)
encapsulation (wrapping class)
abstraction (hides implemention , shows functionality)
'''