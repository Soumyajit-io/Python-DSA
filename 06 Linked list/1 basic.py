class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class SinglyLL:
    def __init__(self,head=None):
        self.head =head

    def insertatbeg(self,value):
        temp=Node(value)
        temp.next = self.head
        self.head=temp

    def insertatmid(self,value,x):
        temp = Node(value)
        t1 = self.head

        while(t1.next!=None):
            if (t1.data == x):
                temp.next=t1.next
                t1.next = temp
            t1=t1.next


    
    def insertatend (self,value):
        temp = Node(value)
        if (self.head != None):
            t1=self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next=temp
        else:
            self.head = temp

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if t1.data == value:
            self.head=t1.next
        while(t1.next!=None):
            if t1.data == value:
                prev.next = t1.next
                return
            else:
                prev = t1
                t1=t1.next
        if t1.data==value:
            prev.next=None

    def printLL(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

l = SinglyLL()
l.insertatend(30)
l.insertatend(20)
l.insertatend(10)
l.insertatbeg(99)
l.insertatmid(65,20)
l.deleteLL(20)
l.deleteLL(99)
l.deleteLL(10)
l.printLL()