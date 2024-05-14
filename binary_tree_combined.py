class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_leftchild(self, leftchild):
        if self.left is None:
            self.left = leftchild
        else:
            print("you are overwriting")
            self.left = leftchild
        return

    def add_rightchild(self, rightchild):
        if self.right is None:
            self.right = rightchild
        else:
            print("you are overwriting")
            self.right = rightchild
        return

    def inorder_traversal(self, last_node, arr=[]):
        if last_node.left:
            self.inorder_traversal(last_node.left)
        arr.append(last_node.data)
        if last_node.right:
            self.inorder_traversal(last_node.right)
        return arr

    def height(self):
        if self.left and self.right:
            return (1 + max(self.left.height(), self.right.height()))
        elif self.left and self.right is None:
            return (1 + self.left.height())
        elif self.left is None and self.right:
            return (1 + self.right.height())
        else:
            return 0

    def is_BST(self):
        lst = self.inorder_traversal(self, [])
        for i in range(len(lst) - 1):
            if lst[i] <= lst[i + 1]:
                pass
            else:
                return False
        return True

    def isbalancedBST(self):
        flag = True
        if self.left and self.right:
            if abs(self.left.height() - self.right.height()) > 1:
                flag = False
                return False
            else:
                if self.left.isbalancedBST() is True:
                    self.right.isbalancedBST()
        elif self.left and self.right is None:
            if self.left.height() > 1:
                flag = False
                return False
            else:
                pass
        elif self.right and self.left is None:
            if self.right.height() > 1:
                flag = False
                return False
            else:
                pass
        if flag == True:
            return True
        else:
            return False


a = Binary_Tree(7)
a1 = Binary_Tree(5)
a2 = Binary_Tree(9)
a11 = Binary_Tree(2)
a111 = Binary_Tree(1)
a112 = Binary_Tree(3)
a21 = Binary_Tree(8)
a22 = Binary_Tree(10)
a12 = Binary_Tree(6)
a.add_leftchild(a1)
a.add_rightchild(a2)
a1.add_leftchild(a11)
a11.add_leftchild(a111)
a11.add_rightchild(a112)
a2.add_leftchild(a21)
a2.add_rightchild(a22)
a1.add_rightchild(a12)
print(a.inorder_traversal(a))
print(a.height())
print(a.is_BST())
print(a.isbalancedBST())


class stack:
    def __init__(self, l):
        self.l = l

    def push(self, element):
        self.l.append(element)
        return

    def pop(self):
        if len(self.l) > 0:
            self.l.pop(-1)
        else:
            print("operation not possible")
        return

    def top(self):
        if len(self.l) > 0:
            return self.l[-1]
        else:
            print("operation not possible")

    def isempty(self):
        if len(self.l) > 0:
            return False
        else:
            return True


def postfix_evaluation(expression):
    operators = ["+", "-", "*", "/"]
    s = stack([])
    for i in range(len(expression)):
        if expression[i] in operators:
            var1 = int(s.top())
            s.pop()
            var2 = int(s.top())
            s.pop()
            if expression[i] == "+":
                s.push(var1 + var2)
            elif expression[i] == "-":
                s.push(var1 - var2)
            elif expression[i] == "*":
                s.push(var1 * var2)
            elif expression[i] == "/":
                s.push(var1 / var2)
        else:
            s.push(expression[i])
    return s.top()


exp = "28+41+*"
print(postfix_evaluation(exp))


def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        left, right = [], []
        mid = len(l) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    arr += left[i:]
    arr += right[j:]
    return arr


# Example:
l = [3, 423, 342, 643, 465, 1, 45]
sorted_l = merge_sort(l)
print(sorted_l)


def quick_sort(l):
    if len(l) > 1:
        pivot = l[len(l) // 2]
        lower_list = [x for x in l if x < pivot]
        middle_list = [x for x in l if x == pivot]
        upper_list = [x for x in l if x > pivot]
        l = quick_sort(lower_list) + middle_list + quick_sort(upper_list)
        return l
    else:
        return l


print(quick_sort(l))


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return self.data


class playlist:
    def __init__(self, head):
        self.head = None

    def add_song(self, title, year, duration):
        new_song = song(title, year, duration)
        if self.head is None:
            self.head = new_song
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_song
        return

    def print_playlist(self):
        arr = []
        if self.head is None:
            return arr
        else:
            last_node = self.head
            while last_node.next:
                arr.append(last_node)
                last_node = last_node.next
            arr.append(last_node)
            return arr


class song:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration


class queue:
    def __init__(self, l):
        self.l = l

    def eneque(self, data):
        self.l.append(data)
        return

    def dequeue(self):
        if len(self.l) >= 1:
            self.l.pop(0)
        else:
            print("operation not possible")
        return


class graph:
    def __init__(self, dic_graph, nodes_list):
        self.dic_graph = dic_graph
        self.nodes_list = nodes_list


# node object inside dictionary

def bfs(gr):
    explore = queue([])
    visited_list = []
    explore.eneque(gr.nodes_list[0])
    while True:
        if len(explore.l)>=1:
            visited_list.append(explore.l[0])
            for i in range(len(gr.dic_graph[explore.l[0]])):
                if gr.dic_graph[explore.l[0]][i] not in visited_list and gr.dic_graph[explore.l[0]][i] not in explore.l:
                    explore.eneque(gr.dic_graph[explore.l[0]][i])
            explore.dequeue()
        if len(visited_list)==len(g.nodes_list):
            break
    return visited_list
a=node("a")
b=node("b")
c=node("c")
d=node("d")
e=node("e")
f=node("f")
g=node("g")
h=node("h")
dic_graph={a:[b,c,d],b:[e],c:[b,d],d:[b],e:[f],f:[g],g:[b,h],h:[a]}
nodes_list=[a,b,c,d,e,f,g,h]
g=graph(dic_graph,nodes_list)
visited_list=bfs(g)
for i in range(len(visited_list)):
    print(visited_list[i])








