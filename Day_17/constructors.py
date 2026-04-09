
'''class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f"Hello {self.username}")

k=Instagram("keerthi","keerthi@2004")
k1=Instagram("karthik","karthik@10")

#encapsulation (public)
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]
k=Instagram('keerthi',"keerthi@2004")
print("Before updating:",k.username)
k.username="karla"
print("After updating:",k.username)

#encapsulation (private)
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password=new_password
k=Instagram('keerthi',"keerthi@2004")
print("Before updating:",k.get_password())
k.set_password("karla@06")
print("After updating:",k.get_password())

#encapsulation (protected)
class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]

    @property
    def myposts(self):
        return self._posts
    @myposts.setter
    def myposts(self,postname):
        self._posts.append(postname)
k=Instagram('keerthi',"keerthi@2004")
print("Before updating",k.myposts)
k.myposts="sun.png"
print("After updating:",k.myposts)

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print(self.title,self.author,self.price)

b=Book("xyz","abc",100)
b.display()

class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_annual_salary(self,base_salary):
        total=base_salary*12
        return  total

e=Employee("Keerthi",20000)
print(e.calculate_annual_salary(20000))'''

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        avg=sum(self.marks)/len(self.marks)
        if(avg<35):
            print("fail")
        else:
            print("pass")
s=Student("keerthi",[68,37,48,27,19])
s.average()




