'''Estruturas lógicas: and, or, not, is

Operadores unários:
    -not, is
Operadores de binários:
    -abd, or

Regras de funcionamento: 

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou otro precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for false vira True
Pra o 'is', o valor é comparado com um segundo
#####

ativo= False
logado= False
if ativo or logado:
    print('Bem vido usuário')
else:
    print('Você precisa ativar sua conta')

#####

ativo= False
logado= False
if not ativo:
    print('você precisa ativar sua conta')
else:
    print('Bem vindo usuário')

'''
