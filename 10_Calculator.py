num1 = float(input("Enter first no."))
op = input("Enter operator")
num2 = float(input("Enter second no"))

if op =='+':
    print(num1+num2)
elif op =='-':
    print(num1-num2)
elif op =='/':
    print(num1/num2)
elif op =='*': 
    print(num1*num2)
else:
    print("Invalid Operator")

