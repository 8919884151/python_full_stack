
'''#Bubble sort
n=int(input("Enter number of elements:"))
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n-i-1):
        if l[j]%2==0 and l[j+1]%2==0:
            if(l[j]<l[j+1]):   # > for ascending order for descending order if(l[j]<l[j+1])
                l[j],l[j+1]=l[j+1],l[j]
                c=c+1
print(l)
print(c)

#insertion sort
def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
        c=c+1
    return a
a=[9,4,2,7]
print(insertion_sort(a))

def insert_into_sorted(a,x):
    a.append(0)
    i=len(a)-2
    while i>=0 and a[i]>x:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=x
    return a
a=[1,3,5,7]
x=4
print(insert_into_sorted(a,x))'''

#Quick sort

def quick_sort(a):
    if len(a)<1:
        return a
    pivot=a[0] #pivot=a[-1]
    left=[]
    right=[]
    for i in a[1:]: #for i in a[:-1]
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[pivot]+quick_sort(right)
a=[5,2,4,1,0]
print(quick_sort(a))



