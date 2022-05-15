#Como tratar um dicionário
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
print(f'O {pessoas["nome"]}, tem  {pessoas["Idade"]} anos.') #Aqui é importante que você declare com chave mas na hora que for imprimir ou referenciar deve-se usar com cochetes

#como printar as chaves, os valores ou os dois
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
print(pessoas.keys()) #para imprimir as chaves
print(pessoas.values()) #para imprimir os valores
print(pessoas.items()) #para imprimir a chave com cada valor

#Como acessar as chaves,  valores e itens 
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
for k in pessoas.keys(): #para cada uma das chaves imprima
    print(k)

for v in pessoas.values(): #para cada um dos valores imprima
    print(v)

for k, v in pessoas.items(): #para cada chave e valor imprima '''k=chave e v==valor'''
    print(f'{k}={v}')

#Para apagar um determinada chave
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
del pessoas['Sexo'] #Aqui mais uma vez usando o cochete ao invés de chave
for k, v in pessoas.items():
    print(f'{k}={v}')

#Para substituir um valor dentro de uma chave
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
pessoas ['nome']= 'Leandro' #Aqui mais uma vez usando o cochete ao invés de chave
for k, v in pessoas.items():
    print(f'{k}={v}')

#Para adicionar um chave e um valor
pessoas= {'nome': 'Marcelo', 'Sexo': 'M', 'Idade': 20}
pessoas['peso'] = 100
for k, v in pessoas.items():
    print(f'{k}={v}')

#Criando um dicionário dentro de uma lista
brasil=[]
estado1={'UF': 'Rio De Janeiro', 'Sigla': 'RJ'}
estado2={'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1] ['sigla']) #aqui estou falando para que na lista 1 ele printe a sigla. 

#Usando for
estado={}
brasil=[]
for c in range (0,3):
    estado['UF']=str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #este .copy serve para criar uma cópia do dicionário e daí não adicionar o o original, é tipo o [:] de listas
for e in brasil: #aqui é pra imprimir cada estado com cada sigla
    for v in e.values():
        print(v, end='')
    print()