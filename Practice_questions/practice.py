
#leap year
'''n=int(input())
if (n%400==0) or (n%4==0 and n%100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#check if number is 3-digit number
n=int(input())
if 100<=n<=999:
    print("3-digit number")
else:
    print("Not a 3 digit number")

    
#vowel or consonant
ch=input()
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("consonant")


#check if a number is between 1 and 100
n=int(input())
if 1<n<100:
    print("in range")
else:
    print("out of range")

#check if a number is square of another number
n=int(input())
s=int(input())
if n is s*s:
    print(f"{n} is square of {s}")
else:
    print(f"{n} is not square of {s}")

#check if two strings ar equal
s1=input()
s2=input()
if s1==s2:
    print("Equal")
else:
    print("Not equal")

#check prime number
n=int(input())
if n<=1:
    print("Not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        else:
            print("Prime")
            break

#check if a character is uppercase
ch=input()
if 'A'<=ch<='Z':
    print("Uppercase")
else:
    print("Lowercase")

#check 4-digit even number
n=int(input())
if n%2==0 and 1000<=n<=9999:
    print("4-digit even number")
else:
    print("Not")



#sum of digits
n=int(input())
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum=sum+r
print(sum)

#length of number
n=int(input())
c=0
while n!=0:
    n=n//10
    c=c+1
print(c)

#reverse of a number
n=int(input())
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)

#palinrome of number
n=int(input())
num=n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
if num==rev:
    print("Palindrome")
else:
    print("Not palindrome")

#factorial of a number
n=int(input())
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)

#anagram
s1=input()
s2=input()
if(sorted(s1)==sorted(s2)):
    print("Anagram")
else:
    print("not anagram")

#first non repeating character
s=input()
for i in s:
    if s.count(i)==1:
        print(i)
        break
    else:
        ("all are repeating characters")

#fibonacci series
a=0
b=1
n=int(input())
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

#amstrong number
import math
n=int(input())
num=n
c=len(str(num))
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum=sum+math.pow(r,c)
if(num==sum):
    print("armstrong")
else:
    print("not armstrong")

#strong number
n=int(input())
num=n
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum=sum+i
if num==sum:
    print("Strong number")
else:
    print("not")

#check if a character is consonant
ch=input()
if ch not in "AEIOUaeiou":
    print("consonant")
else:
    print("vowel")

#check if a string start with a vowel
s=input()
if s[0] in "AEIOUaeiou":
    print("yes")
else:
    print("no")

#valid traingle
a,b,c=input().split(",")
if (a+b)>c or (b+c)>a or (a+c)>b:
    print("Valid")
else:
    print("invalid")

#compare length of two strings
s1,s2=input().split()
if(len(s1)>len(s2)):
    print("first string is longer")
elif(len(s2)>len(s1)):
    print("Second string is longer")
else:
    print("both are equal in length")

#chech is the number is perfect square
import math
n=int(input())
s=math.sqrt(n)
if s==int(s):
    print("Perfect square")
else:
    print("NOt a perfect square")


#factorial of a number using for loop
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


#multiplication table of a number
n=int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


#count number which is divisible by 3
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
print(c)

#multiples of 5 upto n
n=int(input())
n1=5
for i in range(1,n+1):
    print(f"{n1*i}")

#maximum of three number using for loop
l=list(map(int,input().split()))

max=l[0]
for n in l:
    if n>max:
        max=n
print(max)

#sum of first n natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#print numbers from N to 1 using while loop
n=int(input())
while n>=1:
    print(n)
    n=n-1

#sum of prime numbers up to n
n=int(input())
sum=0
for i in range(1,n):
    if(i%i==0):
        sum=sum+i
    print(sum)

#product of digits of a number using while loop
n=int(input())
p=1
while(n!=0):
    r=n%10
    n=n//10
    p=p*r
print(p)

#print numbers both divisible by 3 and 5
n=int(input())
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)

#gcd of 2 numbers
a=int(input())
b=int(input())
while b:
    a,b=b,a%b
print(a)


#numbers divisible by 7 using for loop
n=int(input())
for i in range(7,n,7):
    print(i)

#print even numbers in reverse order using while loop
n=int(input())
while n>=1:
    print(n)
    n=n-2

#sum of first n odd numbers using for loop
n=int(input())
sum=0
for i in range(1,n,2):
    sum=sum+i
print(sum)

#armstrong number using for loop
import math
n=input()
l=len(n)
num=int(n)
sum=0
for i in range(l):
    sum=sum+i**l
print(sum)
if num==sum:
    print("Armstrong")
else:
    print("not")


#traingles
a=int(input())
b=int(input())
c=int(input())
if (a==b==c):
    print("Equilateral")
elif (a!=b!=c and b!=c!=a and c!=a!=b):
    print("scalene")
else:
    print("isoceles")

#Classify a character as: vowel, consonant, digit, special character
ch=input()
if ch in "aeiouAEIOU":
    print("Vowel")
elif ch in "0123456789":
    print("digit")
elif ch in "@#$%^&_":
    print("Special character")
else:
    print("Consonant")

#BMI Calculator and CategoryQuestion: Take height and weight, compute BMI and classify (Underweight, Normal,Overweight, Obese).
h=float(input("Enter in m"))
w=int(input("Enter in kg"))
if 1.00<h<2.00 and 20<w<55:
    print("Undderweight")
elif 1.50<h<2.50 and 56<w<75:
    print("Overweight")
elif 3.10<h<4.00 and 50<w<60:
    print("Normal")
else:
    print("Obese")


#Electricity bill calculator based on units used
n=int(input())
sum=0
if n<=100:
    sum=n*1
elif n<=200:
    sum=(100*1)+(n-100)*2
else:
    sum=(100*1)+(100*2)+(n-200)*3
print(sum)

#Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char)
s=input()
special=False
digit=False
uppercase=False
if (len(s)>=8):
    for i in s:
        if i in "@#$%^&*/_":
            special=True
        elif i in "0123456789":
            digit=True
        else:
            uppercase=True
    if(special and digit and uppercase):
        print("Strong password")
else:
    print("weak password")

#ATM Withdrawal Simulation
a=int(input())
wa=int(input())
if (a>=500 and wa%100==0 and a%100==0):
    print("Success")
else:
    print("insufficient balance")

#Ticket fare calculator with age-based discounts
age=int(input())
cost=0
if age<5:
    cost=0
elif age<18:
    cost=cost+100*0.50
else:
    cost=cost+100*0.70
print(cost)

#24-hour to 12-hour time converter  
time=input()
h,m=map(int,time.split(":"))
if (h<12):
    period="AM"
else:
    period="PM"

if (h==0):
    dt=12
elif(h>12):
    dt=h-12
else:
    dt=h

print(f"{dt}:{m}{period}")

#Currency denomination counter
n=int(input())
den=[2000,500,100,20,10,5,2,1]
for i in den:
    if n>=i:
        c=n//i
        n=n%i
        print(f"{c}*{i}")


#Movie ticket price based on day and age
day=input().lower()
age=int(input())
price=0
if(day=="saturday" or day=="sunday"):
    if (age<12):
        price=price+200*0.50
    else:
        price=price+200
else:
    if (age<12):
        price=price+150*0.50
    else:
        price=price+150

print(price)

#Grade college admission based on marks in 3 subjects
m1=int(input())
m2=int(input())
m3=int(input())
avg=(m1+m2+m3)/3
if avg>90 and m1>70 and m2>70 and m3>70:
    print("admit")
elif avg>=80:
    print("waitlist")
else:
    print("reject")

#Check if a number is perfect
n=int(input())
num=n
sum=0
for i in range(1,n//2+1):
    if(n%i==0):
        sum=sum+i
print(sum)
if(sum==num):
    print("perfect")
else:
    print("not")

#Check if four digits form a lucky number (sum of first two == last two)
n=input()
sum1=0
sum2=0
l=len(n)
for i in range(0,l//2):
    sum1=sum1+int(n[i])
print(sum1)
for j in range(l//2,l):
    sum2=sum2+int(n[j])
print(sum2)
if(sum1==sum2):
    print("lucky")
else:
    print("Not lucky")

#Classify number as Single, Double, or Triple digit
n=int(input())
if(1<=n<10):
    print("single digit")
elif 10<=n<=99:
    print("double digit")
elif 100<=n<=999:
    print("triple digit")

#Validate time input (HH:MM format)
h,m=input().split(":")
if(0<=int(h)<=23 and 0<=int(m)<=59):
    print("valid")
else:
    print("invalid")

#Identify duplicate digits in a 3-digit number
n=input()
n1=len(set(n))
if n1==len(n):
    print("Unique")
else:
    print("duplicates present")

#Weekday classifier (Input: 1–7, Output: Day type)
n=int(input())
d={1:"monday",2:"Tuesday",3:"wednesday",4:"thursday",5:"friday", 6:"saturday",7:"sunday"}
if n<=5:
    print(f"{d[n]}-weekday")
else:
    print(f"{d[n]}-weekend")

#Student attendance eligibility (> 75% to write exam)
n,t=input().split("of")
n1=int(n)
t1=int(t)
if ((n1/t1)*100>75):
    print("eligible")
else:
    print("not eligible")'''

#Validate mobile number (10 digits, starts with 6–9)
n=input()
if len(n)==10:
    if 6<=int(n[0])<=9:
        print("valid")
    else:
        print("invalid")
else:
        print("invalid")


























