from config_arquivos import *
from design import *


ark= "banco_dados.txt"
if not arquivoExiste(ark):
    criarArquivo(ark)
while True:
    resposta=menu(['\033[032mVer pessoas cadastradas','Cadastrar nova pessoa','deletar pessoa','sair do sistema\033[m'])
    if resposta == 1:
        lerArquivo(ark)

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome=str(input('Diga o nome: '))
        idade=leiaint('Diga a idade: ')
        cadastrar(ark, nome, idade)
    
    elif resposta == 3:
        deletar_dado(ark)
   
    elif resposta == 4:
        print('programa encerrado! :)')
        break
    else:
        print('ERRO, OPÇÃO INVÁLIDA!')