#class relationship:
#1.aggregation(Has-a)
#2.inheritance(Is-a)
#inheritance example: car---is a--->vehicle
#smartphone---is a--->product
#aggregation example: customer---has a--->address
class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,name,gender,city,pincode,state):
        self.name=name
        self.gender=gender
        self.address.city=city
        self.address.pincode=pincode
        self.address.state=state
        return "successfully edited profile!"
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def __str__(self):#created this method because of print statement later,if didnt do this,there is no face of object to print
        return (f"city:{self.city}\n"
                f"pincode:{self.pincode}\n"
                f"state:{self.state}\n")
    '''
    def change_address_menu(self):
        userinput=int(input("Enter 1 to change city\n"
                            "Enter 2 to change pincode\n"
                            "Enter 3 to change state\n"))
        if userinput==1:
            self.change_city()
        elif userinput==2:
            self.change_pincode()
        elif userinput==3:
            self.change_state()
        else:
            print("invalid choice!\n"
                  "please re-enter your choice")
            self.change_address_menu()
    def change_city(self):
        user_input=input("Enter new city:")
        self.city=user_input
        print("city changed successfully!")
    def change_pincode(self):
        user_input = input("Enter new pincode:")
        self.pincode = user_input
        print("pincode changed successfully!")
    def change_state(self):
        user_input = input("Enter new state:")
        self.state = user_input
        print("state changed successfully!")
    '''
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_state
        print("address successfully changed!")
add=Address("patiala",147001,"punjab")
cust=customer("harsh","M",add)
print(cust.address)
print(cust.address.city)#takes address from cust object-which is add object and takes city attribute from  add object, then prints it
cust.address.change_address("Ropar",140001,"Punjab")
print(f"\n{cust.address}")
