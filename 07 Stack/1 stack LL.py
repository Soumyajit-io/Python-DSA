class node:
    def __init__(self,val):
        self.v = val
        self.n = None


class myStack:
    def __init__(self, n):
        self.head = None
        self.size =0


    def isEmpty(self):
        return self.size ==0

    
    def push(self, x):
        # Insert x at the top of the stack
        t =node(x)
        t.n=self.head
        self.head=t
        size+=1


    
    def pop(self):
        # Removes an element from the top of the stack
        if self.size==0 :
            print("underflow")
            return
        head = head.n
        size-=1


    
    def peek(self):
        # Returns the top element of the stack
        print(self.head.v)