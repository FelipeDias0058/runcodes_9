#Função que determina a mensagem dependendo do sexo
def mensagem(nome, sexo):
    if '1' in sexo:
        print(f'Ilmo Sr. {nome}')
    if '2' in sexo:
        print(f'Ilma Sra. {nome}')
        

def main():
    #Entrada de nome e sexo
    nome = input("")
    sexo = input("")

    #Executa a função 'mensagem'
    mensagem(nome, sexo)

if __name__ == '__main__':
    main()
