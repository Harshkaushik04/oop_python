class Parent:
    def _init_(self,name):
        self.identity=name
    def location(self):
        print("inside parent class")
class Child(Parent):#constructor inherited from parent class
    def location(self):
        print("inside child class")
obj1=Parent("hi")
obj2=Child("hello")
obj1.location()
obj2.location()