lista = [2, 4, 5, 4, 7, 3, 4, 7, 3, 9]
dicionario = {}

for numero in lista:
    if numero in dicionario:
        dicionario[numero] += 1
    else:
        dicionario[numero] = 1

numero_mais_count = 0
for numero, count in dicionario.items():
    print(f'O {numero} apareceu {count} vezes.')

mais_frequente = max(dicionario, key=dicionario.get)
print(f'O número que aparece com mais frequência é o : {mais_frequente}')

print('Nuno Rocha')