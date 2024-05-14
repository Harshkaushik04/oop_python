import random
#problem_1
class Calculator:
    def add(self,a1,a2,a3=0):
        return a1+a2+a3
    def subtract(self,a1,a2):
        return a1-a2
    def multiply(self,a1,a2,a3=1):
        return a1*a2*a3
    def divide(self,a1,a2):
        return a1/a2
#problem_2
class Account:
    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0
    def deposit(self,money):
        self.balance+=money
        return
    def withdraw(self,money):
        if money>=self.balance:
            self.balance-=money
        else:
            print("not enough money to withdraw")
        return
    def display(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self,account_number,interest_rate):
        Account.__init__(self,account_number)
        self.interest_rate=interest_rate
    def calculate_interest(self,years):
        return self.balance*self.interest_rate*years/100
#problem_3
class Dice:
    def __init__(self,sides=6):
        self.sides=sides
    def roll(self):
        return random.randint(1,self.sides)

class Dice_game(Dice):
    def __init__(self,number,sides=6):
        Dice.__init__(self,sides)
        self.number=number
    def stats(self):
        lst=[]
        for i in range(self.number):
            lst.append(self.roll())
        number_of_1=0
        number_of_2=0
        number_of_3=0
        number_of_4=0
        number_of_5=0
        number_of_6=0
        for x in lst:
            if x==1:
                number_of_1+=1
            elif x==2:
                number_of_2+=1
            elif x==3:
                number_of_3+=1
            elif x==4:
                number_of_4+=1
            elif x==5:
                number_of_5+=1
            elif x==6:
                number_of_6+=1
        print(f"number of 1:{number_of_1},probability={number_of_1/self.number}\nnumber of 2:{number_of_2},probability={number_of_2/self.number}\nnumber of 3:{number_of_3},probability={number_of_3/self.number}\nnumber of 4:{number_of_4},probability={number_of_4/self.number}\nnumber of 5:{number_of_5},probability={number_of_5/self.number}\nnumber of 6:{number_of_6},probability={number_of_6/self.number}")
#problem_4
