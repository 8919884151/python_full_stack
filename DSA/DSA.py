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
    print()

#counting characters in the string
name=input("Enter the name: ")
c=0
for i in range(len(name)):
    c=c+1
print(c) #keerthi count =7 

#printing even index characters
name=input("Enter name: ") #keerthi
for i in range(len(name)):
    if(i%2==0):
        print(name[i]) #keti

#count occurances of specific character
name=input("Enter name: ") #keerthi
ch=input("Enter char: ") #e
c=0
for i in range(len(name)):
    if(name[i]==ch):
        c=c+1
print(c) #2

#count vowels in string
name=input("Enter name: ")
c=0
for i in range(len(name)):
    if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o'or name[i]=='u' or name[i]=='A' or name[i]=='E' or name[i]=='I' or name[i]=='O' or name[i]=='U' ):
        c=c+1
print(c)

#another program of vowels count
c=0
name=input("Enter name: ") #keerthi
vowels="aeiouAEIOU"
for i in range(len(name)):
    if name[i] in vowels:
        c=c+1
print(c) #3

#number count in string
name=input("Enter name: ") #k3h4j5h6
c=0
numbers="0123456789"
for i in range(len(name)):
    if name[i] in numbers:
        c=c+1
print(c)             #4

#sum of numbers in string
name=input("Enter name: ")  #k3h4j5h6
sum=0
numbers="0123456789"
for i in range(len(name)):
    if name[i] in numbers:
        sum+=int(name[i])
print(sum)               #18
 
 #Reverse the string
name=input("Enter name: ")  #code
reverse=""
for i in range(len(name)):
    reverse=name[i]+reverse
print(reverse)            #edoc    

#reversing the string using slicing
name=input("Enter name: ")
print(name[::-1])  
 
#check palindrome
n=input("Enter name: ")
reverse=n[::-1]
if(n==reverse):
    print("palindrome")
else:
    print("not palindrome")

#count words
n=input("Enter the sentence: ")
c=1
for i in range(len(n)):
    if(n[i]==" "):
        c=c+1
print(c)

#check anagrams
s1=input("Enter string1: ")
s2=input("Enter string2: ")
l1=sorted(s1)
l2=sorted(s2)
if(l1==l2):
    print("Anagram")
else:
    print("Not anagram")'''








    







    






