'''
n=input()
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def rem(a,b):
    return a%b
def floor(a,b):
    return a//b
if '+' in n:
    a,b=n.split('+')
    print(add(int(a),int(b)))
elif '-' in n:
    a,b=n.split('-')
    print(subtract(int(a),int(b)))
elif '*' in n:
    a,b=n.split('*')
    print(multiply(int(a),int(b)))
elif '+' in n:
    a,b=n.split('/')
    print(divide(int(a),int(b)))
elif '%' in n:
    a,b=n.split('%')
    print(rem(int(a),int(b)))
elif '//' in n:
    a,b=n.split('//')
    print(floor(int(a),int(b)))'''



            
