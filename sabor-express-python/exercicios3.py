numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Carlos', 'Pedro', 'Vini', 'Tony']
anos = [2001, 2024]

print('\nNúmeros')
for numero in numeros:
    print(numero)

print('\nNomes')
for nome in nomes:
    print(nome)

print('\nAnos')
for ano in anos:
    print(ano)

print('\nSoma dos Ímpares')
soma = 0
for numero in numeros:
    if numero%2 != 0:
        soma = soma+numero
print('\nA soma dos ímpares de 1 a 10 é: ',soma)

print('\nOrdem Decrescente dos números de 1 a 10')
decrescente = []
valor_anterior = 0
for numero in numeros:
    if numero > valor_anterior:
        decrescente.insert(0, numero)
        valor_anterior = numero

for numero in decrescente:
    print(numero)

numero_selecionado = int(input('\nDigite um número para ver a sua tabuada: '))
for i in range(1, 11):
    resultado = i * numero_selecionado
    print(f'{i} x {numero_selecionado} = {resultado}')


print('Somando números e validando')
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


print('Média dos Números')
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")