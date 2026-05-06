def calculate(num1,operator,num2):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            return "error :divison by zero is not allowed"
        return num1/num2
    else:
        return "error :invalid Operator"
    
def main():
    while True:
        try:
            num1=float(input("enter first number "))
            operator=input("enter operator:")
            num2=float(input("enter second number "))

            result=calculate(num1,operator,num2)

            print("result:",result)
        except ValueError:
            print("Error: invalid input ")

        choice=input("do you want to continue ?:")
        if choice!='y':
            print("bye")
            break

if __name__=="__main__":
    main()





        
            