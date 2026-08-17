class node :
    def __init__(self,v):
        self.v = v
        self.n = None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def inseratend(self,val):
        temp = node(val)
        if self.size ==0:
            self.head = self.tail = temp
        else:
            self.tail.n=temp
            self.tail= temp
        self.size+=1
    def insertatbeg(self,val):
        temp = node(val)
        if self.size==0:
            self.head = self.tail = temp
        else:
            temp.n = self.head
            self.head=temp
        self.size+=1

    def insertatidx(self,val,idx):
        if idx==self.size :
            self.inseratend(val)
        elif idx==0:
            self.insertatbeg(val)
        elif(idx<0 or idx>self.size):
            print("Invalid idx")
        else:
            temp = node(val)
            t1=self.head
            
            for _ in range(0,idx-1):
                t1 = t1.n
            temp.n =t1.n
            t1.n=temp
            self.size+=1

    def get (self,idx):
        if idx==0:
            return self.head.v
        elif(idx==self.size-1):
            return self.tail.v
        elif(idx<0 or idx>=self.size):
            print("Invalid")
        else:
            t1=self.head
            for _ in range(0,idx):
                t1 = t1.n 
            return t1.v
    def deleteathead(self):
        if self.size==0:
            return 
        self.head=self.head.n
        self.size -=1
    def deletetail(self):
        t = self.head
        while(t.n!=self.tail):
            t= t.n
        self.tail= t.n=None
        self.size -=1
    def deleteidx(self,idx):
        if idx<0 or idx >=self.size:
            print("invalid idx")
        elif(idx == 0):
            self.deleteathead()
        elif(idx==self.size-1):
            self.deletetail()
        else:
            t1 = self.head
            for _ in range(0,idx-1):
                t1 = t1.n
            t1.n = t1.n.n
            self.size -=1
    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.v,end =" ",sep=" ")
            temp = temp.n
        print("\n")


a = LL()
a.inseratend(50)
a.display()
a.insertatbeg(5000)
a.display()
a.inseratend(10)

a.display()
a.deletetail()
a.display()
a.insertatbeg(500)
a.display()
a.insertatidx(99,1)
a.display()
a.insertatidx(99,1)
a.display()
a.deleteathead()
a.display()
print("idx 1: ", a.get(1))
a.deleteidx(1)
a.display()
a.insertatbeg(500)
a.display()
print("size: ", a.size)
