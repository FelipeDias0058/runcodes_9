#A função exibe na tela o tipo do(s) caractere(s) inserido(s) 
def f_caractere(txt):
    if txt in 'aeiouAEIOU':
        print("vogal")
    elif txt in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        print("consoante")
    elif txt.isnumeric():
        print("número")
    else:
        print("símbolo")
        
def main():
    #Entrada de Dados
    txt = input("")

    #Execução da fumção
    f_caractere(txt)

if __name__ == '__main__':
    main()
