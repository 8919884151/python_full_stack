'''products=["Rice","Wheat","Sugar","Milk","Eggs","oil","tea_powder","salt","bread","soap"]
prices=[160,25,40,30,96,150,500,25,43,35]
print("wELCOME TO GROCERY STORE")
print("Here are the available products")
print('Index'.ljust(6," "),'Products'.ljust(10," "),'Prices'.ljust(6," "))
for i in range(10):
    print(str(i+1).ljust(6," "),products[i].ljust(10," "),str(prices[i]).ljust(6," "))
    
items=list(map(int,input("Enter the list number :").split(" ")))
total_amount=0
print("Selected items are")
for item in items:
    print(products[item-1],prices[item-1])
    total_amount+=prices[item-1]
print("Total amount =",total_amount)
print("Thank you for shopping")

#functions
def wish(name):
    print(f" hello {name}")
wish("keerthi")

#positional arguments
def display(username,email,password):
    print("Uername:",username)
    print("Email:",email)
    print("Password:",password)

display("keerthi","keerthi@gmail.com","k@2004")

#keyword arguments
def display(username,email,password):
    print("Uername:",username)
    print("Email:",email)
    print("Password:",password)

display(username="keerthi",email="keerthi@gmail.com",password="k@2004")'''







    


