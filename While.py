'''O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão Booleana é toda a expressão onde o resultado é verdadeiro ou falso 


n=1
while n<10:
    print(n)
    n=n+1
'''
#ex.2
"Enquanto 'r' for diferente de 'sim' continue  "
'''r=''
while r !='sim':
    r=input('Deseja continuar?')'''



#saindo de loops com break

'''
Utiliza-se o break para sair de loops de maneira projetada
'''
#ex com for
'''for n in range (1, 11):
    if n==6:
        break
    else:
        print(n)
print('Sai do loop')'''

#ex com while

while True:
    c=input('Digite sair para sair: ')
    if c=='sair':
        break
print('Saiu do loop')