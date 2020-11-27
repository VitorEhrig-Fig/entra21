numeros = []
numeros_primos = []
def digitando_o_numero():
    global numero_indicado
    numero_indicado = int(input('digite um numero'
                                '\n>>> '))

def criando_os_numeros():
    for i in range(2, (numero_indicado+1)):
            num = i
            numeros.append(num)

def divisivel(x, y):
    divisao = x%y
    return divisao

def separando_os_numeros(): # valtando implementar for
    for i in numeros:
        if i%2 != 0 or i == 2:
            if i%3 != 0 or i == 3:
                if i%5 != 0 or i == 5:
                    if i%7 != 0 or i == 7:
                        numeros_primos.append(numeros.pop(numeros.index(i)))

        
def funcao():
    digitando_o_numero()
    criando_os_numeros()
    numeros_primos.append(numeros.pop(numeros.index(2)))
    numeros_primos.append(numeros.pop(numeros.index(3)))
    separando_os_numeros()
    print(numeros_primos)

funcao()