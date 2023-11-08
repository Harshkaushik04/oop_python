class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:                               #linked list is object formed of multiple nodes
    def __init__(self):
        self.head=None                           #self.head is object of class node
    def append(self,data):                       #append method is adding node at the end of linked list
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
        last_node=self.head
        if self.head is None:
            self.head=node(data)
            return
        else:
            variable_1=last_node.data
            variable_2=data
            last_node.data=variable_2
            while last_node.next:
                flag=True
                last_node=last_node.next
                variable_2=last_node.data
                last_node.data=variable_1
                if last_node.next is not None:
                   last_node=last_node.next
                   variable_1=last_node.data
                   last_node.data=variable_2
                   flag=False
                if flag==True:
                    final_variable=variable_2
                else:
                    final_variable=variable_1
            last_node.next=node(final_variable)
llink=Linked_list()
llink.append('A')
llink.append('B')
llink.print_list()
llink.prepend('wow!')
llink.print_list()












