class myStack:
    def __init__(self, n):
        self.l=[0]*n
        self.top = -1
        self.size=n
    
    def isEmpty(self):
        return self.top ==-1

    
    def isFull(self):
        return self.top==self.size-1


    
    def push(self, x):
        # Insert x at the top of the stack
        if self.top == self.size-1:
            print("Overflow")
            return
        else:
            self.top+=1
            self.l[self.top]=x

    
    def pop(self):
        # Removes an element from the top of the stack
        if self.top ==-1:
            print("underflow")
            return
        self.top-=1
        return self.l[self.top]

    
    def peek(self):
        # Returns the top element of the stack
        if self.top ==-1:
            print("st is empty")
            return
        return self.l[self.top]