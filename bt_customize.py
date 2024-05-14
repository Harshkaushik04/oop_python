class Binary_Tree:
    def __init__(self, node_value):
        self.node_value = node_value
        self.left_child = None
        self.right_child = None

    def add_child_left(self, value):
        if self.left_child is not None:
            print("overwriting")
            self.left_child = value
        else:
            self.left_child = value

    def add_child_right(self, value):
        if self.right_child is not None:
            print("overwriting")
            self.right_child = value
        else:
            self.right_child = value

    def preorder_traverse(self):
        print(self.node_value)
        if self.left_child is not None:
            self.left_child.preorder_traverse()
        if self.right_child is not None:
            self.right_child.preorder_traverse()

    def postorder_traverse(self):
        if self.left_child is None and self.right_child is None:
            print(self.node_value)
        elif self.left_child is None and self.right_child is not None:
            self.right_child.postorder.traverse()
            print(self.node_value)
        else:
            self.left_child.postorder_traverse()
            if self.right_child is not None:
                self.right_child.postorder_traverse()
            print(self.node_value)

    def inorder_traverse(self,last_node,arr=[]):
        if last_node.left_child:
            last_node.inorder_traverse(last_node.left_child)
        arr.append(last_node.node_value)
        if last_node.right_child:
            last_node.inorder_traverse(last_node.right_child)
        return arr
    def height(self):
        if self.left_child is not None and self.right_child is not None:
            return 1 + max(self.left_child.height(), self.right_child.height())
        elif self.left_child is None and self.right_child is not None:
            return 1 + self.right_child.height()
        elif self.left_child is not None and self.right_child is None:
            return 1 + self.left_child.height()
        else:
            return 0

    def is_BST(self):
        x = self.inorder_traverse()
        flag = 0
        for i in range(0, len(x) - 1):
            if x[i] > x[i + 1]:
                print("NOT A BST")
                flag += 1
                break
        if flag == 0:
            print("IT IS A BST")

    def is_balanced_BST(self):
        flag = 0
        if self.left_child is not None and self.right_child is not None:
            if abs(self.left_child.height() - self.right_child.height()) <= 1:
                if self.left_child.is_balanced_BST() is False:
                    flag += 1
                else:
                    self.right_child.is_balanced_BST()
            else:
                flag += 1
                return False
        elif self.left_child is None and self.right_child is not None:
            if self.height() > 1:
                flag += 1
                return False
            else:
                self.right_child.is_balanced_BST()
        elif self.left_child is not None and self.right_child is None:
            if self.height() > 1:
                flag += 1
                return False
            else:
                self.left_child.is_balanced_BST()
        if flag == 0:
            return True
        else:
            return False


a = Binary_Tree(50)
a1 = Binary_Tree(30)
a2 = Binary_Tree(20)
a11 = Binary_Tree(15)
a21 = Binary_Tree(8)
a22 = Binary_Tree(10)
a12 = Binary_Tree(10)
a.add_child_left(a1)
a.add_child_right(a2)
a1.add_child_left(a11)
a2.add_child_left(a21)
a2.add_child_right(a22)
a1.add_child_right(a12)
'''a.inorder_traverse()
print(a.height())
a.is_BST()
print(a.is_balanced_BST())
a.postorder_traverse()'''
print(a.inorder_traverse(a))
