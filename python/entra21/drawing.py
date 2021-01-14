from random import randrange
# , 'Georgia', 'Leonardo'
alunos = ['Amanda', 'Arthur', 'Claudinei', 'Davy', 'Eduarda', 'Fabricio', 'Felipe', 'Gabrieli', 'Helion', 
    'Isadora', 'Jéssica', 'João', 'Julio', 'Karla', 'Kemoel', 'Luana', 'Luiz', 'Marcus', 'Maria',
    'Raul', 'Robinson', 'Thiago', 'Vitor', 'William']
alunos2 = alunos.copy()
def draw(alunos):
    print(len(alunos))
    for i in range(len(alunos)):
        print(f"{alunos.pop(randrange(len(alunos)))} -> {alunos2.pop(randrange(len(alunos2)))}")
draw(alunos)


