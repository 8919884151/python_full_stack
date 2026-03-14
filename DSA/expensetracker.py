
expenses=[]
def add_expenses():
    name=input("Enter expense name: ")
    amount=input("Enter expense amount: ")
    expense={
        "name":name,
        "amount":amount
    }
    expenses.append(expense)
    print("Expense added")

def view_expenses():
    for expense in expenses:
        print(expense["name"],"-",expense["amount"])

def show_menu():
    print("Expense tracker")
    print("1.Add expense")
    print("2.View expenses")
    print("3.Exit")

def main():
    while True:
        show_menu()
        ch=input("Enter your choice: ")
        if ch=='1':
            add_expenses()
        elif ch=='2':
            view_expenses()
        elif ch=='3':
            print("Exit")
            break
        else:
            print("invalid choice")
main()

