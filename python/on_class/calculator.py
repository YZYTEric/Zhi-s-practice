def add(num1:int, num2:int):
    return num1 + num2

def subtract(num1:int, num2:int):
    return num1 - num2

def multiply(num1:int, num2:int):
    return num1 * num2

def divide(num1:int, num2:int):
    return num1 / num2

def calculator():
    print("select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ["1","2","3","4"]:
        print("invalid input, try again.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    #float的含义是为了表示全数，显示小数点后一位
    if choice == "1":
        print("result:", add(num1, num2))
    elif choice =="2":
        print("result: ", subtract(num1, num2))
    elif choice =="3":
        print("result: ", multiply(num1, num2))
    elif choice =="4":
        print("result: ", divide(num1, num2))
    else:
        print("invalid input.")
calculator()


