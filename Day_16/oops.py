
class Flipkart:
    #class attribute
    discount=10
    @classmethod
    def updateDiscount(cls,new_discount):
        cls.discount=new_discount

    @staticmethod
    def welcome():
        print("Welcome to the flipkart")

    def my_orders(self,order_id):
        #Instance attribute
        self.order_id=order_id
        print(f"You have order these product with id:{self.order_id}")

#class att,class meth,inst att,inst meth,static=>object
#class att,class meth,static=>class
a=Flipkart()
b=Flipkart()

print(a.discount)

print(Flipkart.discount)
#a.myorders(1)

#print(a.order_id)

a.updateDiscount(20)
a.my_orders(2)
a.welcome()

Flipkart.updateDiscount(20)
Flipkart.welcome()