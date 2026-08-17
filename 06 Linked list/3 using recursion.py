class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def display(head):
    if head == None:
        return 
    print(head.data)
    display(head.next)

a= Node(10)
b= Node(100)
c= Node(1000)

a.next=b
b.next=c
display(a)


