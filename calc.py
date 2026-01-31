class calculator():
    def sum(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiple(a,b):
        return a*b
    def divide(a,b):
        return a/b
a=int(input("Enter the number a"))
b=int(input("Enter the number b"))
print("1.sum 2.subtract 3.multiple 4.divide")
choice=int(input("Enter the choice:"))
if choice==1:
    print(calculator.sum(a,b))
elif choice==2:   
    print(calculator.subtract(a,b)) 
elif choice==3: 
    print(calculator.multiple(a,b)) 
elif choice==4:    
    print(calculator.divide(a,b))   
elif choice==5:
    print("THANK YOU")    