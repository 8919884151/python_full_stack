'''#printing numbers 1 to 10
def display(n):
    if n>10:
        return 
    print(n)
    display(n+1)
display(1)

def display(n):
    if n>10:
        return 
    display(n+1)
    print(n)
display(1)

def display(name,i):
    if i==len(name):
        return 
    print(name[:i+1])
    display(name,i+1)
display("Python programming",0)

def display(s,n):
    if n<=0:
        return 
    display(s,n-1)
    print(s*n)
display("abc",5)

def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+1])
    display(s,i+1,n)
display("abcdef",0,3)

def display(l,i,sum):
    if i==len(l):
        return sum
    #print(l[i],sum)
    return display(l,i+1,sum+l[i])
print(display([1,2,3,4,5],0,0))

def display(l,i,s):
    if i==len(l):
        return s
    #print(s)
    return display(l,i+1,s+l[i])

print(display(['python','java','html','css','flask'],0," "))'''

#pass by value (immutable ) andpass by reference(mutable)
def display(n):
    n=n+(8,9)
    print("Inside: ",n)
n=(1,2,3,4)
display(n)
print("Outside: ",n)

def display(n):
    n=n+10
    print("Inside: ",n)
n=10
display(n)
print("Outside: ",n)

def display(n):
    n=n+12
    print("Inside: ",n)
n=12.5
display(n)
print("Outside: ",n)

def display(n):
    n=n+"keerthi"
    print("Inside: ",n)
n="karla"
display(n)
print("Outside: ",n)

def display(n):
    n.extend([5,6])
    print("Inside: ",n)
n=[1,2,3,4]
display(n)
print("Outside: ",n)

def display(n):
    n[7]=8
    print("Inside: ",n)
n={1:2,3:4,5:6}
display(n)
print("Outside: ",n)

def display(n):
    n.add(8)
    print("Inside: ",n)
n={1,2,3,4}
display(n)
print("Outside: ",n)
