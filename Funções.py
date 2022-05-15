#trabalhando com funções
#Use replace('o que é pra ser substituído', 'pelo que vai ser substituido') para substuir algo


def soma(a, b):
    s=a+b
    print(f'A soma de A+B={s}')

soma(4,5)
soma(2,6)
soma(2,9)

#empacotamento com tuplas
def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 5, 7, 3, 1)

#desempacotamento
def soma(*valores):
    s=0
    for num in valores:
        s=s+num
        print(f'somando os valores {valores} temos {s}')

#usando listas
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos=pos+1

valores=[6, 4, 7, 2, 1]
dobra(valores)
print(valores)



#####################################Funções parte 2##################################################

def contador (i, f, p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """#abre aspas tripas para colocar o que é cada parâmetro para mostrar no help. Isto é uma Docstring
    c=i
    while c<=f:
        print(f'{c}', end='')
        c=c+p
        print('Fim')

help(contador) #vai mostrar o que é o contador(i, f, p) e vai aparecer o que coloquei nas aspas triplas

#Parâmetros opcionais
def soma(a=0, b=0, c=0): #aqui eu estou dizendo que mesmo que no programa eu não defina o valor de a, b ou c ele tem a opção de valer 0 ou outro valor adicionado
    s=a+b+c
    print(f'A soma vale {s}')
soma(2,4)


#Escopo de varáveis
def teste():
    x=8 
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
#programa principal
n=2
print(f'No programa principal, n vale {n}') #aqui vai funcionar pois é um escopo global e funciona tanto na função quanto no prog. principal
print(f'No programa principal, x vale x {x}') #isso daqui não vai funcionar porque x não é um escopo global e sim local pois ela só foi definida na função

#dois escopos iguais com valores diferentes
def funçao():
    global n1 #
    n1=4
    print(f'N1 dentro da func vale {n1}') #aqui n1 é um escopo local
n1=2
funçao()
print(f'N1 fora da func vale {n1}') #e aqui é global, o programa irá considerar os dois

#Trasformando o n1 local em global
def funçao():
    global n1 #aqui estou dizendo que não é para o n1 da função ser local, daí o n1 de fora recebe o valor de n1 que coloquei de dentro da função
    n1=4
    print(f'N1 dentro da func vale {n1}') 
funçao()
print(f'N1 fora da func vale {n1}') 

#retorno de valores
def somar(a=0, b=0, c=0):
    s= a+b+c
    return s

r1= somar(1, 4, 5)
r2= somar(5,2)
r3= somar(2)
print(f'Os resultados foram {r1}, {r2}. e {r3}')