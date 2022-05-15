#16. Tipo Float

#Tipo real, decimal

#casas decimais

#Obs: Separados de casas decimais na programação é o ponto e não a vírgula

# Errado do ponto de vista do Float, mas gera uma tupla
valor=1, 44
print(valor)
print(type(valor))

#certo do ponto de vista Float
valor=1.44
print(valor)
print(type(valor))

#É possível fazer uma dupla atribuição
valor1, valor2=1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um float para um int
#Converter valores float para inteiros ou inteiros para float,
# basta que nós definimos uma variável e em seguida imprima, como: res=float(valor) ou como tá abaixo
#OBS:Nós perdemos precisão de float para inteiro
res=int(valor)
print=(res)
print(type(res))

#podemos trabalhar com númeoros complexos 