from design import *

def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')
        a= open(nome, 'at') 
        a.close()
    except:
        print('Houve um ERRO na criação')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('Erro ao ler')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
def cadastrar(ark, nome='desconhecido', idade=0):
    try:
        a= open(ark, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print('Adicionado!')
            a.close()

def deletar_dado(ark):
    try:
        escolha_user=int(input('Diga uma linha para a exclusão: '))

        with open(ark, 'rt') as dados:
            linhas=dados.readlines()
        cont=1
        with open(ark, 'wt') as dados1:
            for dado in linhas:
                if cont != escolha_user:
                    dados1.write(dado)
                cont+=1
        return print('~~~ Pessoa deletada ~~~')
    except:
        return print('Erro, digite apenas números!')
