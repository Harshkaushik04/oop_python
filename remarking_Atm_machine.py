class Atm:
    def __init__(self):
        self.__pin=''
        self.__balance=0
        self.menu()
    def menu(self):
        user_input = int(input("how would you like to proceed:\n"
                               "Enter 1 to create pin\n"
                               "Enter 2 to deposit\n"
                               "Enter 3 to withdraw\n"
                               "Enter 4 to check balance\n"
                               "Enter 5 to change pin\n"
                               "Enter 6 to exit\n"))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            pass
    def create_pin(self):
        if self.__pin!='':
            self.__pin=input("Enter pin:")
            print(f"pin:{self.__pin}")
            print("pin successfully created!")

