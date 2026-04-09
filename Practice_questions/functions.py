
import math

'''def area(r):
    return math.pi*r*r
print(area(3))

def ctof(t):
    return t*(9/5)+32
print(ctof(37))

def length(s):
    c=0
    for i in s:
        c=c+1
    return c
print(length("keerthi"))

def add(l,x):
    l.append(x)
    return l
l=list(map(int,input().split(" ")))
x=int(input())
print(add(l,x))

def double(l):
    l1=[]
    for i in l:
        l1.append(i*2)
    return l1
l=list(map(int,input().split(" ")))
print(double(l))

def sor(l):
    l.sort()
    return l
l=list(map(int,input().split()))
print(sor(l))

def cl(l):
    l.clear()
    return l
l=list(map(int,input().split()))
print(cl(l))

def re(l,x):
    l.remove(x)
    return l
l=list(map(int,input().split()))
x=int(input())
print(re(l,x))

def up(d,k,v):
    d[k]=v
    return d
d=eval(input())
k=input()
v=int(input())
print(up(d,k,v))

def reverse(s):
    return s[::-1]
s=input()
print(reverse(s))

f=lambda x:x*2
print(f(5))

l=[1,2,3]
f=list(map(lambda x:x*x,l))
print(f)

l=[1,2,3]
f=list(filter(lambda x:x%2==0,l))
print(f)

from functools import reduce
f=lambda a,b:a if a>b else b
print(f(20,30))

n=input().split()
t=[eval(i) for i in n]
s=sorted(t,key=lambda x:x[1])
print(s)

l=["hi","hello","bye"]
f=list(map(lambda x:x.upper(),l))
print(f)

l=["hi","hello","bye"]
f=list(map(lambda x:len(x),l))
print(f)

s="apple" 
f=lambda x:True if x[0] in "aeiou" else False
print(f(s))

l=["hi","hello","bye"]
f=list(filter(lambda x:len(x)>3,l))
print(f)'''


