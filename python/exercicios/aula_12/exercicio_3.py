def lados_triandulo():
    """
        dando input e criando a lista
    """
    global triangulo
    triangulo = []
    a = float(input('lado a'
                    '\n>>> '))
    triangulo.append(a)
    b = float(input('\nlado b'
                    '\n>>> '))
    triangulo.append(b)
    c = float(input('\nlado c'
                    '\n>>> '))
    triangulo.append(c)
    triangulo.sort()

def descobrindo_se_e_triangulo():
    """
        descobrindo se é triângulo ou n
    """
    global soma
    soma = triangulo[0] + triangulo[1]
    if soma >= triangulo[2]:
        print('\né um triângulo\n')
    
    else:
        print('n é um triângulo')

def tipo_triangulo():
    if triangulo[0] == triangulo[1] and triangulo[1] == triangulo[2]:
        print('é um triângulo equilatero')
    
    elif triangulo[0] == triangulo[1] or triangulo[1] == triangulo[2] or triangulo[2] == triangulo[0]:
        print('é um triângulo isóseles')
    
    elif triangulo[0] != triangulo[1] and triangulo[1] != triangulo[2] and triangulo[2] != triangulo[0]:
        print('é um triângulo escaleno')

def funcao(): # poderia chamar fora ai as funcoes ficariam mais portaveis
    lados_triandulo()
    descobrindo_se_e_triangulo()
    tipo_triangulo()

funcao()