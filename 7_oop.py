class customer:
    counter=1 #static/class variable:created for numbering customers
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sno=customer.counter #static variables are accessed by class_name.static_name(whearas,instance variable are accessed through self.instance_name
        customer.counter+=1
    def __str__(self):
        return f"{self.sno}. {self.name},{self.age}"
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
#static
#instance variable:different values for all abjects
#static/variable:variable for which value is same for all variables
#static variable is initialised outside the constructor and instance variables inside constructor

#encapsulation of static variable(counter):
class new:
    __counter=1 #static/class variable:created for numbering customers
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sno=new.__counter #static variables are accessed by class_name.static_name(whearas,instance variable are accessed through self.instance_name
        new.__counter+=1
    def __str__(self):
        return f"{self.sno}. {self.name},{self.age}"
    def intro(self):
        print(f"my name is {self.name}\n"
              f"my age is {self.age}\n"
              f"your shop is nice")
    @staticmethod #keyword for using static method
    def counter_getter():
        print(new.__counter) #class.static_var is method to access static variable(different from instance var)
    @staticmethod
    def counter_setter(new_counter):
        if type(new_counter)==int:
            new.__counter=new_counter
            print("counter changed!")
        else:
            print("not allowed!")
new.counter_getter() #this would have given error if counter_getter was a normal method
new_customer=new("nitish",32)
new_customer.counter_getter()
new_customer.counter_setter(3)
new_customer.counter_getter()

#in case of dealing with static variables, use static methods, wich do not take self as argument
#the reason we do this is because normal methods do not work on classes,it only works on objects, because self can take value of objects only, not class
#hence we use static method which doesnt include use of self
#if counter_getter wasnt static(means if it was a normal method), then we would have got error on new.get_counter(), as self cant take new class into it, it needs an object, and new isnt an object