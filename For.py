'''nome= Geek University
lista= [1, 3, 5, 7, 9]
numeros= range(1, 10)

#Exemplo de for 1 (iterando em string)
for letra in nome:
    print (letra)

#Exemplo de for 2 (iterando sobre um lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre um range)
for numero in range (1, 10):
    print(numero)

qtd=int(input('Quantas vezes esse loop deve rodar? '))
soma=0
for n in range (1, qtd+1):
    num=int(input('Informe o valor {}/{} valor: '.format(n, qtd)))
    soma=soma + num
print('A soma será {}'.format(soma))

'''