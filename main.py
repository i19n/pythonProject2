x=float(input('Первое число'))
y=float(input('Второе чвисло'))

operation=input('Операция')

result=None
if operation=='+':
    result= x+y
elif operation=='-':
    result=x-y
elif operation=='*':
    result=x*y
elif operation=='/':
    result=x/y
else:
    print('Ошибка')


if result is not None:
    print('Результат', result)