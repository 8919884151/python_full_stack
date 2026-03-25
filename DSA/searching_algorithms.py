
#linear search
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


#binary search
def binary_search(a,x):
    if(len(a)==0):
        return -1
    start=0
    end=len(a)-1
    mid=(start+(end-start))//2
    while(start<=end):
        if(x<a[mid]):
            end=mid-1
        elif(x>a[mid]):
            start=mid+1
        else:
            return mid
    return a[mid]
a=[1,5,8,3,7,10]
x=7
print(binary_search(a,x))
