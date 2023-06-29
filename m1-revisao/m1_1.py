n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 == n2 and n1 == n3:
    print('Todos os números são iguais.')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('"Existem pelo menos dois números iguais')
else:
    print('Todos os números são diferentes')

    print('Nuno Rocha')