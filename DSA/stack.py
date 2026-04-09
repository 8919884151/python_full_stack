
#stack data structure (follows last in first out)
#push->adding an element into stack
#pop->removing an element
#peek->top element
#isempty->checking whether stack is empty or not
#size->count of elements in stack
#Creating stack in three types
#1.by using class and object
#2.by using list built in functions
#3.by using deque(double ended queue)

class Stack:
    def __init__(self):
        self.stack=[]
    

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack:",s.stack)
print("top:",s.peek())
print("Pop:",s.pop())
print("Size:",s.size())
print("Is empty:",s.is_empty)

#creating stack using deque()
from collections import deque
stack=deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print("pop",stack.pop())
print("peek:",stack[-1])




    
