class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:#linked list is object formed of multiple nodes
    def __init__(self):
        self.head=None
        self.count=None #self.head is object of class node
    def append(self,data): #append method is adding node at the end of linked list
        if self.head is None:
            self.head=node(data)
            return
        else:
            last_node=self.head
            while last_node.next is not None:
                last_node=last_node.next
            last_node.next=node(data)
    def print_list(self):
        if self.head is None:
            print('empty list')
        else:
            last_node=self.head
            while last_node.next:
                print(last_node.data)
                last_node=last_node.next
            print(last_node.data)
    def prepend(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        return
    def search(self,data):
        last_node=self.head
        self.count=0
        flag=False
        while last_node.next:
            if last_node.data==data:
                print("found")
                print(f"position:{self.count}")
                flag=True
                break
            self.count+=1
            last_node=last_node.next
        if last_node.data==data and flag==False:
            print("found")
            print(f"position:{self.count}")
        def get_at_position(self,position):
            self.count=0
            last_node=self.head
            while self.count<position and position<self.getsize():
                last_node=last_node.next
                self.count+=1
                if self.count==position:
                    print(last_node.data)
            if position>=self.getsize():
                print("invalid position")
#testing
A=Linked_list()
A.append('a')
A.append('b')
A.append('c')
A.append('d')
A.print_list()
print('printed!')
A.prepend('wow!')
A.print_list()
A.search("d")

class stack():
    def __init__(self):
        self.head=None
        self.count=None
    def push(self,element):
        new_node=node(element)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def remove(self):
        last_node=self.head
        self.head=last_node.next
        last_node.data=None
    def getsize(self):
        last_node=self.head
        self.count=1
        while last_node.next:
            self.count+=1
        print(self.count)
        return self.count
    def top(self):
        print(self.head)
    def isempty(self):
        if self.getsize==0:
            print("empty")
        else:
            print("not empty")
    def display(self):
        if self.getsize!=0:
            last_node=self.head
            while last_node.next:
                print(last_node)
                last_node=last_node.next
            print(last_node)
        else:
            print("empty")
    def print_stack(self):
        last_node=self.head
        while last_node.next:
            print(last_node.data)
            last_node=last_node.next
        print(last_node.data)
#testing
print("stack:")
B=stack()
B.push("a")
B.push("b")
B.push("c")
B.push("d")
B.print_stack()
print("removing element:")
B.remove()
B.print_stack()

class bt_node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree():
    def __init__(self):
        self.head=None
        self.level=None
        self.position=[]
    def find(self,positions):#positions is a list
        last_node=self.head
        l=0
        while l<len(positions):
            if positions[l]==0 and last_node.left is not None:
                last_node=last_node.left
            elif positions[l]==0 and last_node.left is None:
                print("invalid position")
                break
            if positions[l]==1 and last_node.right is not None:
                last_node=last_node.right
            elif positions[l]==1 and last_node.right is None:
                print("invalid position")
                break
        return last_node
    def add(self,data,positions): #positions is a list
        new_node=bt_node(data)
        if self.head is None:
            self.head=new_node
            self.level=0
            self.position=0
        else:
            last_position=positions[-1]
            new_positions=positions[:-1]
            last_node=self.find(new_positions)
            if last_position==0:
                last_node.left=new_node
            elif last_position==1:
                last_node.right=new_node
    def print(self):
        positions=[]
        if self.head==None:
            print("empty")
        else:
            last_node=self.head
            used_positions=[]
            while last_node.left: #for leftmost_position
                last_node=last_node.left
                positions.append(0)
            used_positions.append(positions)
            print(last_node.data)
            while True:
                while positions in used_positions:
                    positions.pop(-1)
                    if positions not in used_positions:
                        last_node=self.find(positions)
                        print(last_node.data)
                        used_positions.append(positions)
                if last_node.right:
                    positions.append(1)
                    last_node=self.find(positions)
                while positions not in used_positions:
                    print(last_node.data)
                    last_node=self.find(positions)
                    used_positions.append(positions)
                    if last_node.right:
                        positions.append(1)
                    last_node=self.find(positions)
                if last_node.left:
                    positions.append(0)
                    last_node=self.find(positions)
                while positions not in used_positions:
                    pass





