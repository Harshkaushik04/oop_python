#what are magic methods:
'''
special/magic/dunder methods:
constructor is a magic method,can find list of magic methods on google
magic methods: __(predefined)__
these magic methods arent called by an object(like other methods can be),but is called automatically when a certain criterion is fulfilled(automatically triggered)
'''
#constructor use-case explained:
'''
constructor is called only when object is being created
things inside constructor practically are the things you want to be not in control of user(user cant change things of constructor as the constructor code runs automatically as the application is run)
=>things like automatically connect application to database,internet,etc or other pre-data are set in constructor
'''
#self
'''
fundamental principle in oop:
inside class, 1 function cant access another function inside same class/other class.
so, for accessing function of same class, "self" is used
as we know everything is object,hence self is also an object.
#self hi sbi hai
self becomes the object its currently dealing with
=>in every function when we called method self.menu(), we were able to do because self is object Sbi and through object we are able to access function

also, whenever there is no argument inside the function called,the default argument is applied, like when function called on sbi.menu(), then functional argument is by default, sbi
=>this is why when we define function inside class, we keep 1 argument(self) inside function and then when we call it, we keep no argument=>by default it keeps the value of argument as that.

=>basically,self is the means to access a function of a class in another function of same class(cant be done otherwise),=>self is Sbi hai(self hi object hai jis pr currently work kr rhe hai)
'''