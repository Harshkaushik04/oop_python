#encapsulation
#in our atm machine class, both data attributes and methods are accessible, means by writing print(sbi.pin), you can get pin without going through the method
#this is why encapsulation is needed which encapsulates the data attributes-means they cant be accessed from outside class
#atm machine with encapsulation:
class Atm:
    #init is a constructor
    #constructor is a special method inside the class which is execueted as soon as object of that class is defined
    #means for example if there is a print statement inside that method, it is also execueted and output is visible
    def __init__(self): #all data to be defined inside this function
        self.__pin=''
        self.__balance=0
        self.menu()
    def menu(self):
        user_input=int(input("how would you like to proceed:\n"
                         "Enter 1 to create pin\n"
                         "Enter 2 to deposit\n"
                         "Enter 3 to withdraw\n"
                         "Enter 4 to check balance\n"
                         "Enter 5 to change pin\n"
                         "Enter 6 to exit\n"
                         "Enter 7 to exit with wow\n"))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        elif user_input==5:
            self.change_pin()
        elif user_input==6:
            self.exit()
        elif user_input==7:
            self.__hidden_method()
        #made methods on various functionalities:
        #basic logic is to first check if pin is correct or not and if its not correct for 5 consecutive time, then account is temporarily blocked
    def create_pin(self):
        if self.__pin=='':
            user_input=input("Enter pin:")
            self.__pin+=user_input
            print(f"successfully created pin!\n"
                  f"{self.__pin}")
            self.menu()
        else:
            print("pin already created!")
            self.menu()
    def deposit(self):
        i = 0
        while i < 5:
            if self.__pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.__pin:
                    user_input = int(input("How much money to deposit:"))
                    #print(self.__balance) #for checking variable value
                    self.__balance += user_input
                    print(f"successfully deposited {user_input} rupees\n"
                          f"Current balance:{self.__balance}")
                    break
                else:
                    print("Entered wrong pin!")
                i += 1
            else:
                print("create a pin first!")
                break
        if i == 5:
            print("Enter wrong pin 5 times!comeback later!")
        self.menu()
    def withdraw(self):
        i = 0
        flag=0
        while i < 5:
            if self.__pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.__pin:
                    while True:
                        user_input = int(input("How much money to withdraw:"))
                        if user_input<=self.__balance:
                            self.__balance -= user_input
                            print(f"successfully withdrew {user_input} rupees\n"
                                  f"Current balance:{self.__balance}")
                            break
                        else:
                            print("not enough money available to withdraw!")
                            flag=1
                            break
                else:
                    print("Entered wrong pin!")
                    i += 1
            else:
                print("create a pin first!")
                break
            if flag==1:
                break
        if i == 5:
            print("Enter wrong pin 5 times!comeback later!")
        self.menu()
    def check_balance(self):
        i = 0
        while i < 5:
            if self.__pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.__pin:
                    print(f"Current balance:{self.__balance}")
                    break
                else:
                    print("Entered wrong pin!")
                    i += 1
            else:
                print("create a pin first!")
                break
        if i == 5:
            print("Enter wrong pin 5 times!comeback later!")
        self.menu()
    def change_pin(self):
        i=0
        while i<5:
            if self.__pin != '':
                user_input = input("Enter your Current pin:")
                if user_input == self.__pin:
                    new_user_input = input("Enter new pin:")
                    if new_user_input != '':
                        self.__pin = new_user_input
                        print(f"successfully changed pin!\n"
                              f"new pin:{self.__pin}")
                        break
                    else:
                        print("pin cant be empty!\n"
                              "redo the process!")
                else:
                    print("Entered wrong pin!")
                    i+=1
            else:
                print("create a pin first!")
                break
        if i==5:
            print("Enter wrong pin 5 times!comeback later!")
        self.menu()
    def exit(self):
        print("bye!")
    def __hidden_method(self): #method can be hided by putting __ before method name
        print("wow!")
    def get_pin(self): #method to access pin outside class
        return self.__pin
    def set_pin(self,new_pin): #method to change pin set pin ouside the class
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin changed!")
            return new_pin
        else:
            print("not allowed")
sbi=Atm()
#sbi._Atm__balance="abc" #__balance can be accessed through _Atm__balance, thats why by changing its value to string sbi.deposit() will give error
#sbi.__balance="abc" # after encapsulation __balance isnt a attribute anymore, hence we created a new attribute __balance and initialised its value as "abc", it doesnt affect value of _Atm__balance
# =>nothing in python can be truly private
#sbi.deposit()
sbi.set_pin('1234')
print(sbi.get_pin())
#first we hid data by encapsulation and then created methods to access it- because by doing that we get to access data+in the way we want the person to access it
#for example if we want a person to change it only to string, then we can keep condition for that in set method