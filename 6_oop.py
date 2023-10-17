#reference variable
# the variable in which object is stored is called reference variable
#pass by reference
class customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
#usage of custom class s' object inside function(greet)
def greet(inside_customer): #inside_customer is object of class customer
    if inside_customer.gender=="m":
        print("say hi")
        print("hello",inside_customer.name)
    elif inside_customer.gender=="f":
        print("say hello")
        print("hello",inside_customer.name)
    else:
        print("say wow")
        print("hello",inside_customer.name)
cust=customer('harsh','m') #cust is object is class customer
print(cust.name)
greet(cust)


#understanding pass by reference=>reference variable(student_one) is passed into function
class student:
    def __init__(self,name):
        self.name=name
def id_of_student(student_name):
    print(id(student_name))
student_one=student('harsh')
print(id(student_one)) #method 1
id_of_student(student_one)#method 2
#id for both the cases is same=> Aliasing
#Aliasing example:
a=3
b=a
print(id(a))
print(id(b))

#example:
class student_new:
    def __init__(self,name):
        self.name=name
def name_of_student(student_name):
    print(id(student_name))
    student_name.name="nitish"
    print(id(student_name))
    print(student_name.name)

student_two=student_new('harsh')
name_of_student(student_two)
print(student_two.name)
print(id(student_two))

#both have same reuslts because
#when function name_of_student is execueted then name of student is changed to nitish
#and the changes remain intact(when object is edited by function through calling, then it mains edited afterwards), thats why print(student_two.name)="nitish"
#mutability:when an object is edited and it still remains at same address/id then its called mutable(mutable datatypes include list,dictionary,set)
#class ke objects are also mutable=> can verify using id of before editing and after

#checking mutability for list:
def check(l):
    print(id(l))
    l.append(5)
    print(id(l))
l=[1,2,3,4]
check(l)
print(id(l))

#checking immutability of tuple:
def check_tuple(l):
    print(id(l),l)
    l+=(5,)
    print(id(l),l)#address changed=>immutable tuple
L=(1,2,3,4)
check_tuple(L)
print(id(L),L)#same adress as first