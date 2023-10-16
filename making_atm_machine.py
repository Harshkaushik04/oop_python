#functions vs methods:
#methods are functions written inside a class
'''
L=[]
len(L)
L.append(1)
even though both are functions but calling method is different,why?
=>because len is function and append is method, method is always passed like that.
=>append is a method defined inside list class
=>len is universal function,append is inside list class, thats why only list object can access it
'''
class Atm:
    #init is a constructor
    #constructor is a special method inside the class which is execueted as soon as object of that class is defined
    #means for example if there is a print statement inside that method, it is also execueted and output is visible
    def __init__(self): #all data to be defined inside this function
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=int(input("how would you like to proceed:\n"
                         "Enter 1 to create pin\n"
                         "Enter 2 to deposit\n"
                         "Enter 3 to withdraw\n"
                         "Enter 4 to check balance\n"
                         "Enter 5 to change pin\n"
                         "Enter 6 to exit\n"))
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
        #made methods on various functionalities:
        #basic logic is to first check if pin is correct or not and if its not correct for 5 consecutive time, then account is temporarily blocked
    def create_pin(self):
        if self.pin=='':
            user_input=input("Enter pin:")
            self.pin+=user_input
            print(f"successfully created pin!\n"
                  f"{self.pin}")
            self.menu()
        else:
            print("pin already created!")
            self.menu()
    def deposit(self):
        i = 0
        while i < 5:
            if self.pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.pin:
                    user_input = int(input("How much money to deposit:"))
                    self.balance += user_input
                    print(f"successfully deposited {user_input} rupees\n"
                          f"Current balance:{self.balance}")
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
        while i < 5:
            if self.pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.pin:
                    while True:
                        user_input = int(input("How much money to withdraw:"))
                        if user_input<=self.balance:
                            self.balance -= user_input
                            print(f"successfully withdrew {user_input} rupees\n"
                                  f"Current balance:{self.balance}")
                        else:
                            print("not enough money available to withdraw!")
                else:
                    print("Entered wrong pin!")
                    i += 1
            else:
                print("create a pin first!")
                break
        if i == 5:
            print("Enter wrong pin 5 times!comeback later!")
        self.menu()
    def check_balance(self):
        i = 0
        while i < 5:
            if self.pin != '':
                new_user_input = input("Enter your Current pin:")
                if new_user_input == self.pin:
                    print(f"Current balance:{self.balance}")
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
            if self.pin != '':
                user_input = input("Enter your Current pin:")
                if user_input == self.pin:
                    new_user_input = input("correct pin!\n"
                                           "Enter new pin:")
                    if new_user_input != '':
                        self.pin = new_user_input
                        print(f"successfully changed pin!\n"
                              f"new pin:{self.pin}")
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
sbi=Atm()
