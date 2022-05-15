#Tipo string

"""Em Python, um dado é considerado do tipo string sempre que:
Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '41.2'
Estiver entre àspas duplas -> "Ima string", "234", "a", "True", "41.2"
Estiver Entre às simples triplas-> '''uma string''', '''234''', '''a''', '''True'''

nome= 'Marcelo Júnio'
 print(nome)
 printi(type(nome))

nome= "Gina's Bar"
 print(nome)
 print(type(nome))

nome='Angelina \nJolie' (\n fará com que o nome Jolie vá para a linha de baixo)
print(nome)
print(type(nome))

print(nome.upper()) #Deixa a strig toda em maiúsculo

print(nome.lowe())  #Deixa a string em mínuscula

print(nome.lower()) #Transforma em uma lista de strings
"""

#Estiver entre àspas duplas triplas-> """uma string""", """234""",... """41.2"""
# [ 0,   1,   2,  3,   4,   5,   6,   7,   8,  9,   10,  11,  12,  13,  14,]
# ['G', 'e', 'e', k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
"""nome= 'Geek University'
print(nome[0:4]) #Isso é uma lista, vai imprimir Geek, pois ele conta da primeira lista '0' até o 4 contando somente do 0 ao 3

***

print(nome[5;15]) #Isso vai imprimir 'university'. ESSE EXEMPLO E O PRIMEIRO SÂO 'Slice de string

***

print(nome.split()[0]) #Isso vai transformar 'G', 'e', 'e', 'k' em uma lista só e irá imprimir, o mesmo seria feito com 'University se colocasse '1' no lugar de '0'

***

print(nome[::-01]) vai imprimir a lista inteira do 0 ao 15 e o -1 serve para inverter a ordem que será imprimida

print(nome.replace('g', 'p')) vai trocar o g pelo p

"""
