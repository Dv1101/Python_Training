class A:
    def hi(self):
        print("I am class A")

class B(A):
    def helloo(self):
        print("I am class B")

class C(B):
    def dhruv(self):
        c = B()
        c.helloo()
        c.hi()

p1 = C()
p1.dhruv()