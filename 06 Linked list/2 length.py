class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def lengt(head):
    count=0
    print(head)
    while(head!= None):
        count+=1
        head = head.next
    print(head)
    return count

a= Node(10)
b= Node(100)
c= Node(1000)

a.next=b
b.next=c

print(lengt(a))

