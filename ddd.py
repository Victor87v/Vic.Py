#Calculando IMC
for c in range (1,11):
    p= float(input('Digite seu peso: '))
    a= float(input('Digite sua altura: '))
    i= p/a**2
    if i<18.5:
        print('IMC= {}'.format(i))
        print('Abaixo do peso')
        print('-' * 25)
    if 18.5<=i<24.9:
        print('IMC= {}'.format(i))
        print('Peso normal')
        print('-' * 25)
    if 25<=i<29.9:
        print('IMC= {}'.format(i))
        print('Sobrepeso')
        print('-' * 25)
    if 30<=i<34.9:
        print('IMC= {}'.format(i))
        print('Obesidade Grau I')
        print('-' * 25)
    if 35<=i<39.9:
        print('IMC= {}'.format(i))
        print('Obesidade Grau II')
        print('-' * 25)
    if i>=40:
        print('IMC= {}'.format(i))
        print('Obesidade Grau III ou Mórbida')
        print('-' * 25)

