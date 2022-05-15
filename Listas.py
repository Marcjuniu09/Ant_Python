
#para adicionar um item na lista
.apepend('') #adiciona alguma coisa no final da lista
.insert(posição desejada, 'item a ser adicionado') #vai adicionar algum item em alguma outra posição da lista

#para remover algo da lista
del lanche[posição do item] #remove algo da lista e o que tá dentro do cochete é a posição
.pop(posição) #mesma coisa do primeiro mas se você não colocar nada dentro do parenteses ele remove o último
.remove('nome do item') #remove algo pelo nome

#um exemplo com o .remove('')
if 'pizza' in lanche:
    lanche.remove('pizza')
##desta maneira ele só irá remover se tiver o item pizza na lista lanche

#criando uma lista com range
valores=list(range(4,11)) #aqui irá criar uma lista com valores de 4 até o 11 desconsiderando o 11

valores=[8, 2, 5, 4, 9, 3, 0]
valores.sort() #esse comando organiza a lista do maior pro menor
valores.sort(reverse=True) #organiza de forma decrescente
len(valores) #conta quantos elementos tem na lista 

######
num=[2, 5, 9, 1]
num[2]=3 #na posição 2 ele irá deixar de valer 9 e valerá 3
num.append(7) #adicionou o número 7 no final da lista
num.sort(reverse=True) #organizou a lista de forma decrescente
num.insert(2,2) #adicinou o número 2 na posição 2
if 5 in num:
    num.remove(5)#removou o primeiro numero 5 que apareceu na lista
else:
    print('Não achei o número 5')
print(f'Essa lista tem {len(num)} elementos')
########

valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')

#########

valores=[]
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))  #neste estou adicionando manualmente elemnetos a uma lista

#########
a=[2, 3, 4, 7]
b=a[:] #lembre-se que para criar uma cópia de uma lista tem que colocar esses cochetes aí, só igualar não vai funcionar pois qualquer coisa que se muda em uma irá mudar na outra
b[2]=8
print(f'lista A: {a}')
print(f'lista B: {b}')


'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

                                        '''LISTAS PARTE 2'''
# Adicionando uma lista dentro de outra lista e mudando e adicionando uma cópia da mesma em outra lista
lista1=[]
lista1.append('Marc')
lista1.append('40')
lista2=[]
lista2.append(lista1[:]) #aqui estou adicionando uma lista 1 dentro de uma outra lista 2, e para isso é importante que eu faça uma cópia da lista um para que ela não imprima a mesma coisa
lista1[0]='juniu'
lista1[1]= 20
lista2.append(lista1[:]) #olha a cópia aqui de novo
print(lista2)

#imprimindo certos elementos em uma lista aninhada
lista=[['lucas', 22], ['Marc', 20], ['Juniu', 21], ['vuc vuc', 10]]
print(lista['número da lista'] [numero do elemento dentro da lista selecionada])

#usando for
lista=[['lucas', 22], ['Marc', 20], ['Juniu', 21], ['vuc vuc', 10]]
for p in lista:
    print(p[se quiser só um elemento especifico é só colocar a posição aqui]) #se não quiser é só falar pra printar normal mesmo

#um exemplo usando for
galera=[]
dado=[]
totmai=totmen=0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #aqui eu gerei uma cópia para não adicionarem uma lista igual
    dado.clear #limpando a lista para poder adicionar novos dados

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+=1
print(f'Temos {totmai} meiores e {totmen} menores de idade')