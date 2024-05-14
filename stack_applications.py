#from class_stack import stack
class stack:
    def __init__(self,l):
        self.l=l
    def push(self,element):
        self.l.append(element)
    def pop(self):
        self.l.pop(-1)
    def getsize(self):
        return len(self.l)
    def top(self):
        return self.l[-1]
    def isempty(self):
        if len(self.l)==0:
            return "Empty"
        else:
            return "not empty"
    def display(self):
        for i in range(len(self.l)):
            print(self.l[i])
#parenthesis matching
def parenthesis_checking(expression):
    s=stack([])
    flag=True
    for i in range(len(expression)):
        if expression[i]=="(" or expression[i]=="{" or expression[i]=="[":
            s.push(expression[i])
        elif expression[i]==")" or expression[i]=="}" or expression[i]=="]":
            if (s.top()=="(" and expression[i]==")") or (s.top()=="{" and expression[i]=="}") or (s.top()=="[" and expression[i]=="]"):
                s.pop()
            else:
                flag=False
                return "not balanced"
    if flag==True and s.getsize()==0:
        return "balanced"
    else:
        return "not balanced"
#example
input1="[()]"
input2="[(])"
print(parenthesis_checking(input1))
print(parenthesis_checking(input2))
#postfix evaluation
def postfix_evaluation(expression):
    s=stack([])
    operators=["+","-","*","/"]
    for i in range(len(expression)):
        if expression[i] not in operators:
            s.push(expression[i])
        else:
            var1=int(s.top())
            s.pop()
            var2=int(s.top())
            s.pop()
            if expression[i]=="+":
                s.push(var1+var2)
            elif expression[i]=="-":
                s.push(var1-var2)
            elif expression[i]=="*":
                s.push(var1*var2)
            elif expression[i]=="/":
                s.push(var1/var2)
    return s.top()
input_exp="782*+1+"
print(postfix_evaluation(input_exp))