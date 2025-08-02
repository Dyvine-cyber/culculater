num1=float(input("Enter the num1:"))
num2=float(input("Enter the num2:"))
operation = input("Enter the operation (+, -, *, /, %, **): ")
#add
if operation =='+':
    result=num1+num2
    print(f'result:{result}')
elif operation =='-':
    result =num1-num2
    print(f'result:{result}')
elif operation=="/":
    result =num1/num2
    print(f"result:{result}")
elif operation=='%':
    result=num1%num2
    print(f'result:{result}')
elif operation=='*':
    result=num1*num2
    print(f'result:{result}')
elif operation=='**':
    result=num1**num2
    print(f"result:{result}")
else:
    print('invalid operation!')   



