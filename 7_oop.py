class customer:
    counter=1 #static/class variable:created for numbering customers
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sno=customer.counter #static variables are accessed by class_name.static_name(whearas,instance variable are accessed through self.instance_name
        customer.counter+=1
    def __str__(self):
        return f"{self.name},{self.age},{self.sno}"
    def intro(self):
        print(f"my name is {self.name}\n"
              f"my age is {self.age}\n"
              f"your shop is nice")
c1=customer("harsh","18")
c2=customer("nitish","28")
c3=customer("priyam","18")
L=[c1,c2,c3] #collection of objects
#these objects cant be stored inside sets because they can only contain immutable datatypes, but these are muttables
for i in L:
    print(i)
#static keyword
#instance variable:different values for all abjects
#static/variable:variable for which value is same for all variables
#static variable is initialised outside the constructor and instance variables inside constructor