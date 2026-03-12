'''#even or odd
n=int(input("Enter a number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

#maximum of two numbers
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
if (a>b):
    print("maximum number is ",a)
else:
    print("maximum number is ",b)

#using multiple conditions(Example of if/elif/else)
marks=int(input("Enter your marks: "))
if (marks>=90):
    print("Grade O")
elif (marks>=80):
    print("Grade A+")
elif (marks>=70):
    print("Grade A")
elif (marks>=60):
    print("Grade B+")
elif (marks>=50):
    print("Grade B")
else:
    print("Fail")

#Count even numbers from 1 to n
c=0
n=int(input("Enter a value: "))
for i in range(1,n+1):
    if(i%2==0):
        c=c+1
print(c) 

 #count digits in number
n=int(input("Enter a number: "))
c=0
while n>0:
    n=n//10
    c=c+1
print(c)

#using function
def count_digits(n):
    c=0
    while n>0:
        n=n//10
        c=c+1
    return c
def main():
    n=int(input("Enter a number: "))
    print(count_digits(n))
main()


#sum of digits in a number
def sum_of_digits(n):
    sum=0
    while n>0:
        r=n%10
        n=n//10
        sum=sum+r
    return sum
def main():
    n=int(input("Enter a number: "))
    print(sum_of_digits(n))
main()

#reverse of number
n=int(input("Enter a number: "))
rev=0
while n>0:
    r=n%10
    n=n//10     
    rev=rev*10+r
print(rev)

#count even digits in a number
c=0
n=int(input("Enter a number: "))
while n>0:
    r=n%10
    n=n//10
    if(r%2==0):
        c=c+1
print(c)

#looping patterns
n=int(input("Enter number of rows: "))
for i in range(n):               *
    for j in range(i):           * *
        print("*",end=" ")       * * *
    print("*",end="\n")

n=int(input("ENter the number of rows :"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
 
for i in range(1,5,1):
    print("*" *i)

for i in range(5,0,-1):
    print("*"*i)
 
n=int(input("Enter number of rows: "))
for i in range(1,n+1):           1
    for j in range(1,i+1):       1 2
        print(j,end=" ")         1 2 3
    print()

n=int(input("Enter number of rows: "))
for i in range(1,n+1):           1
    for j in range(1,i+1):       2 2
        print(i,end=" ")         3 3 3
    print()

n=int(input("Enter the number of rows: "))
for i in range(n+1,1,-1):      1 2 3
    for j in range(1,i):       1 2
        print(j,end=" ")       1
    print()'''







    






