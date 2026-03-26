
'''a=[]
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)

l=[i for i in range(1,100) if i%2==0]
print(l)

l=[i*i for i in range(1,11)]
print(l)

l=[1,2,3,4,5]
res=[i*i for i in l]
print(res)

s="python"
vol="aeiouAEIOU"
l=["*" if i in vol else i for i in s]
print(l)

l=[7,3,2,5,1,6]
res=['0' if i%2==0 else i for i in l]
print(res)

a=[[1,2,3],[2,3,4]]
l=[i for j in a for i in j]
print(l)

l=[7,3,2,5,1,6]
r={i:l.count(i) for i in l}
print(r)'''

res=(i*i for i in range(1,11))
for x in res:
    print(x)
