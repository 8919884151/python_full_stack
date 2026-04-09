
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
     
    def insert_at_position(self,pos,data):
        new_node=Node(data)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        for _ in range(pos-1):
            if temp is None:
                return 
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node


    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def delete_from_beginning(self):
        if self.head:
            self.head=self.head.next

    def delete_from_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next

        temp.next=None

    def delete_value(self,key):
        if self.head is None:
            return
        if self.head.data==key:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next:
            if temp.next.data==key:
                temp.next=temp.next.next
                return
            temp=temp.next

    def delete_at_position(self,pos):
        if self.head is None:
            return
        if pos==0:
            self.head=self.head.next
            return
        temp=self.head
        for _ in range(pos-1):
            if temp.next is None:
                return
            temp=temp.next

        if temp.next:
            temp.next=temp.next.next

    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    
    #access position
    def get(self,pos):
        temp=self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp=temp.next
        return temp.data if temp else None
    
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next #store next node
            curr.next=prev #reverse linked list
            prev=curr   #move prev
            curr=next_node  #move curr
        self.head=prev
    def has_cycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

l=LinkedList()
l.insert_at_beginning(10)
l.insert_at_beginning(5)
l.insert_at_end(20)
l.insert_at_end(30)
l.display()
l.insert_at_position(2,15)
l.display()
l.insert_at_position(0,2)
l.display()
print(l.get(1))
l.delete_value(30)
l.delete_at_position(3)
print(l.search(20))
l.delete_from_beginning()
l.display()
l.delete_from_end()
l.display()


        
