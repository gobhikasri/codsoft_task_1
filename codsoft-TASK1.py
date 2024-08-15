import math
def operations(choice,num1,num2):
    if(choice==1):
        print("Addition of",num1,"and",num2,"is",num1+num2)  
    elif(choice==2):
        print("Subtraction of",num1,"and",num2,"is", num1-num2)      
    elif(choice==3):
        print("Multiplication of",num1,"and",num2,"is",num1*num2)
    elif(choice==4):
        res=num1/num2
        print("Division of",num1,"and",num2,"is",res) 
    elif(choice==5):
        res=num1%num2
        print("remainder after dividing",num1,"and",num2,"is",res) 
    else:
        res=pow(num1,num2)
        print("Power of",num1,"and",num2,"is",res)

    
repeat=True

print("*** Calculator Operations ***")
print("1.Addtion")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Remainder")
print("6.power")
while repeat:
    choice=int(input("Enter your choice(1 to 6): "))
    if 1<=choice<=6 :
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        operations(choice,num1,num2)
    else:
        print("Enter valid choice!!")
        
    process=input("do you want to continue(yes/no):").strip().lower()
    if process != 'yes':
        repeat=False




