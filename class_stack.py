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
#st=stack([1,2,3,4])
#print(st.getsize())