from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')
 
contatos=list()
 
def adicionar():
    print('\tAdicionar o contato')
    email=input('Digite o E-mail: ')
    if len(dados)>0:
        for contato in contatos:
            if email==contato['email']:
                print('Contato já existe.')
                return True
 
    contatos.append({
        'email':email.lower(),
        'nome':input('Nome: ').strip().capitalize(),
        'sobrenome':input('Sobrenome: ').strip().capitalize(),
        'telefone':input('Telefone: ').strip(),
        'data':date.today().strftime('%d/%m/%Y')
    })
    
 
def alterar():
    
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja alterar: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome do contato: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print('1 - Alterar o nome')
                print('2 - Alterar o telefone')
                print('3 - Voltar')
                escolha=input('... ')
                if escolha==str(1):
                    novo_nome=input('Digite um novo nome para o contato: ')
                    contato['nome']=novo_nome
                    return
            
                elif escolha==str(2):
                    novo_tel=input('Digite um novo telefone para o contato: ')
                    contato['telefone']=novo_tel
                    return
                    
                elif escolha==str(3):
                    return
                    
                else:
                    print('Opção inválida.')
                    return
                    
        print('Não existe usuário cadastrado com o e-mail informado.')    
    else:
        print('Não há contatos registrados na agenda.')
 
def procurar():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome: {contato['nome']} {contato['sobrenome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Data de registro: {contato['data']}")
                return
                
    print('Não há contatos na agenda.')
 
def remover():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja remover: ')
        x=0
        while x<len(contatos):
            if contatos[x]['email']==email:
                contatos.remove(contatos[x])
                return True
            x = x + 1
            
        print('Contato não foi encontrado.')
    else:
        print('Não há contatos na agenda.')
 
def ver():
    if len(contatos)>0:
        contatos_ordenados=sorted(contatos,key=lambda contato:contato['nome']+' '+contato['sobrenome'])
        for indice,contato in enumerate(contatos_ordenados,start=1):
            print(f'Contato {indice}'.center(100,' '))
            print(f"Nome: {contato['nome']} {contato['sobrenome']}")
            print(f"E-mail: {contato['email']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Data de registro: {contato['data']}")
            print()
    else:
        print('Não há contatos registrados na agenda.')
        
 
def menu():
    print('Programa Agenda  '.center(100,' '))
    print('\t1 - Adicionar contato')
    print('\t2 - Alterar contato')
    print('\t3 - Procurar contato')
    print('\t4 - Remover contato')
    print('\t5 - Ver contatos')
    print('\t6 - Sair')
 
def main():
    escolha=''
    while escolha!=str(6):
        menu()
        
        escolha=input('>> ')
        
        if escolha==str(1):
            adicionar()
            
        elif escolha==str(2):
            alterar()
            
        elif escolha==str(3):
            procurar()
            
        elif escolha==str(4):
            remover()
            
        elif escolha==str(5):
            ver()
            
        else:
            if escolha==str(6):
                print('Fim do Programa.')
            else:
                print('Escolha inválida')
 
if __name__ =='__main__':
    main()