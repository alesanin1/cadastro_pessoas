def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('POR FAVOR, DIGITE UM NÚMERO VÁLIDO!')
            continue
        except(KeyboardInterrupt):
            print('USUARIO PREFERIU NÃO DIGITAR ESSE NÚMERO')
            return 0
        else:
            return n

def linha (l=45):
    return '-'*l

def cabeçalho(msg):
    print(linha())
    print(msg.center(45))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'     {c} ~~ {item}')
        c+=1
    print(linha())
    opc=leiaint('Diga sua opção ')
    return opc