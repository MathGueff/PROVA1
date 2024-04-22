lista_numeros = [0,0,0]
for i in range(3):
    num = int(input("Digite um número: "))
    lista_numeros[i] = num

lista_numeros.sort(reverse=True)
print(lista_numeros)