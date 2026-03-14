
#Calculating the based on the course
#This project introduces conditional logic in real world projects,validation,edge case handling
def calculate_fee(course,marks):
    if course=='AI':
        fee=50000
    elif course=='Data science':
        fee=70000
    elif course=='Web development':
        fee=40000
    else:
        return None #invalid course
    

    #discount condition
    if marks>90:
        fee=fee-5000
    return fee

def main():
    course=input("Enter course name:")
    marks=int(input("Enter the marks:"))
    fee=calculate_fee(course,marks)

    if fee is None:
        print("Tnvalid course selected")
    else:
        print("Final fee:",fee)

main()
