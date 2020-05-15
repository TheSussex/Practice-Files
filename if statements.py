
def max_num(num1, num2, num3):
    if num1>= num2 and num1>= num3:
        return num1
    elif num2>= num1 and num2>= num3:
        return num2
    else:
        return num3
    
print(max_num(30, 4, 57))


# new code starts here
# float immediately converts into a number instead of the conventional string
num1 = float(input("Enter first no: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")
