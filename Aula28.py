nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é', nome [:: -1])
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
        
    print('Seu nome tem', len(nome),'letras')  
    print('A primeira letra do seu nome é', nome [0])  
    print('A última letra do seu nome é', nome [-1])
    
else:
    print('Desculpe, você deixou campos vazios.')    