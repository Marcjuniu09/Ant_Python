#Tratamentos de erros
try:  #este comando está dizendo para tentar o programa normal
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r= a/b
except: #caso o comando assima não funcione ele irá mostrar este erro
    print('Tivemos um problema')
else: #Caso funcione ele irá rodar normal
    print(f'O resultado é {r}')
finally: #aqui é pra onde o programa irá se funcionar ou se não funcionar
    print('Volte sempre!')

#printando o tipo de erro

try:  
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r= a/b
except Exception as erro:  #aqui é para printar o erro
    print(f'O problema encontrado foi: {erro.__class__}') #este foi a classe do erro
else: 
    print(f'O resultado é {r}')
finally: 
    print('Volte sempre!')


#printando vários tipos de erros
try:  
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r= a/b
except (ValueError, TypeError):  
    print('Tivemos um problema com os tipos de dados qe você digitou') 
except (ZeroDivisionError):
    print('Não é possivel dividir um número por ZERO')
except (KeyboardInterrupt):
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: 
    print(f'O resultado é {r}')
finally: 
    print('Volte sempre!')