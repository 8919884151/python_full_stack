
#we don't have method overloading in python
#method overiding(same method,same parameters ,parent/child classes)
'''
class Hotstar:
    def __init__(self,username):
        print(f"hi {username} welcome to hotstar")
    def promo(self):
        print("You can watch promos")
    def login(self):
        print("You can login")
    def search(self):
        print("You can search movies")
    
    def movie(self):
        print("You have access to old movies")
    def ads(self):
        print("ads will be run")
    def quality(self):
        print("You can watch videos with limited quality")

class PremiumHotstar(Hotstar):
    def __init__(self,username):
        print(f"hi {username} welcome to hotstar premium")
    def movie(self):
        print("You have access to all the movies")
    def ads(self):
        print("ads won't be run")
    def quality(self):
        print("You can watch videos with high quality")

k=Hotstar("karla")
k.promo()
k.login()
k.search()
k.movie()
k.ads()
k.quality()
k1=PremiumHotstar("Keerthi")
k1.promo()
k1.login()
k1.search()
k1.movie()
k1.ads()
k1.quality()'''

#operator overloading
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
    def __sub__(self,other):
        return self.n-other.n
    def __mul__(self,other):
        return self.n*other.n
    def __lt__(self,other):
        return self.n<other.n
    def __gt__(self,other):
        return self.n>other.n
    def __str__(self):
        return str(self.n)
x=Number(10)
y=Number(20)
print(x+y)
print(x-y)
print(x*y)
print(x<y)
print(x>y)
print(x)