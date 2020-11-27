def ponto():
    global salario_hr, horas, bruto
    salario_hr = float(input('digite seu ganho/h\n'
                    '>>> '))
    horas = float(input('digite quantas hrs trabalhou esse mês\n'
                    '>>> '))
    bruto = salario_hr * horas

def porcentagem(bruto): # não seria nescessario esta variavel aqui
    global porcentagem
    porcentagem = bruto/100
    porcentagem = float(porcentagem)

def funcao():
    ponto()
    porcentagem(bruto) # bruto ja é um variavel global
    imposto_renda = porcentagem*11
    inss = porcentagem*8
    sindicato = porcentagem*5
    liquido = bruto - (imposto_renda + inss + sindicato)
    print(
        f'Salário Bruto : R${bruto}\n'
        f'- Imposto de renda (11%) : R${imposto_renda}\n'
        f'- Inss (8%) : R${inss}\n'
        f'- Sindicato(5%) : R${sindicato}\n'
        f'= R${liquido}\n'
    )

funcao()