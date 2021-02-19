a= int(input('Digite o primeiro valor:'))
b= int(input('Digite o segundo valor:'))
c= int(input('Digite o terceiro valor:'))
delta= b**2 - 4*a*c
print('o delta é', delta)
if delta>0:
    x1= (-b + delta**0.5) / 2.0*a
    x2= (-b - delta**0.5) / 2.0*a
    print('x1=',x1)
    print('x2=',x2)
else: print('Não pode ser calculado')
