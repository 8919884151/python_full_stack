
'''#linear search
def linear_search(a,x):
    if(len(a)==0):
        return -1
    for i in range(len(a)):
        if(a[i]==x):
            return i
    return -1
a=[1,5,8,3,7,10]
x=7
print(linear_search(a,x))

# binary search works on sorted list
#binary search
def binary_search(a,x):
    low=0
    high=len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]==x):
            return mid
        elif(a[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1
a=[1,3,5,7,8,10]
x=3
result=binary_search(a,x)
if result!=-1:
    print(result)
else:
    print("Element not found")

n=int(input("Enter n:"))
a=[]
sum=0
for k in range(n):
    val=int(input("Enter elements: "))
    a.append(val)
    sum=sum+val
s1=0
for i in range(1,n+2):
    s1=s1+i

print("Missing element in list sequence:",s1-sum)

#merge two sorted arrays
def merge_two_sorted(a1,a2):
    result=[]
    i=j=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            result.append(a1[i])
            i=i+1
        else:
            result.append(a2[j])
            j=j+1
    result.extend(a1[i:])
    result.extend(a2[j:])
    return result
a1=[1,3,5]
a2=[2,4,6]
print(merge_two_sorted(a1,a2))

#serach rotated array
def  search_rotated_array(a,target):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if(a[mid]==target):
            return mid

        if a[low]==a[mid]==a[high]:
        low=low+1
        high=high-1
        
        if a[low]<=a[mid]:
            if a[low]<=target<a[mid]:
                high=mid-1
            else:
                low=mid+1

        else:
            if a[mid]<=target<=a[high]:
                low=mid+1
            else:
                high=mid-1

    return -1

a=[4,5,6,7,0,1,2]
target=6
print("Index:",search_rotated_array(a,target))

def linear_search(a,x):
    for i in range(len(a)):
        if (a[i]==x):
            return i
    return -1

a=list(map(int,input("Enter elements ").split()))
x=int(input("Enter target value: "))
result=linear_search(a,x)

if(result!=-1):
    print("Index ",result)
else:
    print("not found")'''

def binary_search(a,x):
    l=0
    r=len(a)-1
    while l<=r:
        mid=(l+r)//2
        if(a[mid]==x):
            return mid
        elif(a[mid]<x):
            l=mid+1
        else:
            r=mid-1
    return -1

a=list(map(int,input("Enter elements: ").split()))
x=int(input("Enter target value: "))
result=binary_search(a,x)
if(result!=-1):
    print("Index :",result)
else:
    print("Not found")





