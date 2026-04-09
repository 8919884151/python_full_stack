
'''import random
print(random.random())
print(random.randint(5,100))
print(random.uniform(1,6))

l=['java','python','html','css']
print(random.choice(l))
print(random.choices(l,k=2))
random.seed(10)
l1=random.shuffle(l)
print(l1)

import sys
print(sys.argv)
print()
print(sys.version)
print()
print(sys.path)
print()
print(sys.exit())
#sys.exit()

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.pow(5,2))
print(math.ceil(12.001))
print(math.floor(12.9999))
print(round(12.999))
print(abs(-3))
print(math.fabs(-3))
print(math.factorial(4))
print(math.gcd(4,2))
print(math.log(10,10))
print(math.sin(math.pi/2))
print(math.cos(60))
print(math.tan(45))
print(math.degrees(30))
print(math.radians(30))

import random
l=[1,2,3,5,2,7]
random.shuffle(l)
print(l)

import collections
s="python programming"
l=[1,2,2,3,8,5,7,4,7,4]
r="this or that or that is this".split()

print(collections.Counter(s))
l1=collections.Counter(l)
r1=collections.Counter(r)
print(l1)
print(r1)

import collections
s="python programming"
res=collections.defaultdict(int)
for i in s:
    res[i]=res[i]+1
print(res)

q=collections.deque([])
q.append(20)
q.append(30)
q.append(60)
q.append(70)
q.append(90)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(80)
print(q)

#reverse deque
q=collections.deque([])
q.appendleft(20)
q.appendleft(30)
q.appendleft(60)
q.appendleft(70)
q.appendleft(90)
q.pop()
q.pop()
q.pop()
q.appendleft(10)
q.appendleft(80)
print(q)'''

import itertools
s="abc"
print(list(itertools.combinations(s,2)))
print(list(itertools.permutations(s,2)))