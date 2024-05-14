class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def _init_(self):
        self.head=None
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=Node(data)
        return
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        return
    def search(self,data):
        if self.head is None:
            print("not in list")
        else:
            flag = False
            last_node=self.head
            count=0
            while last_node.next:
                if last_node.data==data:
                    flag=True
                    return count
                last_node=last_node.next
                count += 1
            if last_node.data==data:
                flag=True
                return count
            if flag==False:
                print("not in list")
    def get_at_position(self,position):
        if self.head is None:
            print("invalid position")
            return
        else:
            flag = False
            last_node=self.head
            count=0
            while last_node.next and position<=count:
                if count==position:
                    flag=True
                    return last_node.data
                count+=1
                last_node=last_node.next
            if count == position:
                flag=True
                return last_node.data
            if flag==False:
                print("invalid position")
                return
    def traversal(self):
        if self.head is None:
            print("Empty")
        else:
            last_node=self.head
            while last_node.next:
                print(last_node.data)
                last_node=last_node.next
            print(last_node.data)
    def delete_at_position(self,position):
        if self.head is None:
            print("invalid position")
        else:
            count=0
            last_node=self.head
            while last_node.next:
                pass
L=Linked_list()
L.append(2)
L.append(3)
L.append(4)
L.prepend(1)
L.traversal()
print(L.search(2))
print(L.get_at_position(1))