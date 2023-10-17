#making fraction datatype/class
class fraction:
    def __init__(self,n,d):
        self.num=n #n and d are instance and num,den are attribute, attributes can be accessed by objects are instances cant be
        self.den=d
    def __str__(self): #execuetes when object is inside print statement
        return f"{self.num}/{self.den}" #return keyword must be used
    def __add__(self,other):#whenever there is + between 2 objects of class fraction,this method is called immediately
        output=fraction(0,1)
        output.num=self.num*other.den+other.num*self.den
        output.den=self.den*other.den
        return output
    def __sub__(self, other):#whenever there is - between 2 objects of class fraction,this method is called immediately
        output = fraction(0, 1)
        output.num = self.num * other.den - other.num * self.den
        output.den = self.den * other.den
        return output
    def __mul__(self, other):#whenever there is * between 2 objects of class fraction,this method is called immediately
        output = fraction(0, 1)
        output.num = self.num * other.num
        output.den = self.den * other.den
        return output
    def __truediv__(self, other):#whenever there is / between 2 objects of class fraction,this method is called immediately
        output = fraction(0, 1)
        output.num = self.num * other.den
        output.den = self.den * other.num
        return output

fr1=fraction(5,6)#(arguments from __init__ method) creating object
print(fr1)
fr2=fraction(4,5)#creating object
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)
print(fr1.num) #you can access attribute of a class, but cant access instance
#another magic method is __str__ which automatically triggeres when the object is inside print statement
#like print(fr)


