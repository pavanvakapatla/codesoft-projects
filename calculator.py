def calculate(n1,n2,op):
    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result =  n1*n2
    elif op == '/':
        result = n1/n2
    elif op=='^':
        result =  n1**n2
    else:
        raise ValueError('Invalid operator')
    if result.is_integer():
        result = int(result)
    return result

calc = True
while calc is True:
    n1 = float(input('Enter first number: '))
    n2 = float(input('Enter second number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    print(n1,op,n2)
    result=calculate(n1,n2,op)
    print('=',result)
    yon = input('Continue? (y/n): ')
    if yon == 'n':
        calc = False