
'''n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if((i+j)%2==0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

n=int(input("Enter n :"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("Enter n :"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

n=int(input("Enter n: "))
for i in range(n,0,-1):
    print("*"*i)

n=int(input("Enter n :"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
    
n=int(input("Enter n :"))
for i in range(n):
    for j in range(n):
        print(" ",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i%2==0 or j%2==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (i+j)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#E
n=int(input("Enter n:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#T
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#H
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if j==0 or i==n//2 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#I
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or i==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    #A
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

   #C
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0  or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

   #F
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()















        





    


