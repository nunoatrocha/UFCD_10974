ingrediente = input('Qual ingrediente quer adicionar no seu pedido: ')

while ingrediente != 'sair':
    print(f'{ingrediente} foi adicionado com sucesso.')
    ingrediente = input('Qual ingrediente quer adicionar no seu pedido: ')

active = True
while active:
    if ingrediente == 'sair':
        active = False
    else:
        print(f'{ingrediente} foi adicionado com sucesso.')
        ingrediente = input('Qual ingrediente quer adicionar no seu pedido: ')


while True:
    if ingrediente == 'sair':
        break
    else:
        print(f'{ingrediente} foi adicionado com sucesso.')
        ingrediente = input('Qual ingrediente quer adicionar no seu pedido: ')
