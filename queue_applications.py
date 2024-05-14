#queue using linked_list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
        return
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        return
    def len(self):
        count=1
        if self.head is None:
            return 0
        else:
            last_node=self.head
            while last_node.next:
               last_node=last_node.next
               count+=1
            return count
    def add_at_position(self,data,position):
        new_node=Node(data)
        if self.head is None and position==0:
            self.head=new_node
        elif self.head is not None and position<=(self.len()-1):
            last_node=self.head
            for i in range(position):
                last_node=last_node.next
            new_node.next=last_node
            if position==0:
                self.head=new_node
        return
    def pop(self):
        if self.head is None:
            return "invalid operation"
        else:
            last_node=self.head
            while last_node.next.next:
                last_node=last_node.next
            last_node.next=None
        return

class queue:
    def __init__(self,linked_list):
        self.head=linked_list.head
    def make_null(self):
        self.head=None
        return
    def front(self):
        return self.head
    def enqueue(self,data):
        new_node=Node(data)
        last_node=self.head
        if self.head is None:
            self.head=new_node
        else:
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
        return
    def dequeue(self):
        last_node=self.head
        self.head=last_node.next
        return
    def empty(self):
        if self.head is None:
            return True
        else:
            return False                                                                                        

