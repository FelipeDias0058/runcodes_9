#Função para o cálculo da média
def f_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def main():
    #Digita as notas individuais
    n1 = float(input(""))
    n2 = float(input(""))
    n3 = float(input(""))
    #Atribui a função 'f_media' à variável 'media_a'
    media_a = f_media(n1, n2, n3)

    #Executa a função 'f_media'
    f_media(n1, n2, n3)

    #Condicionais 'if' que ajustam o resultado da média
    if n3 > 8:
        media_a += 1
    if media_a > 10:
        media_a = 10

    #Mostra na tela a média, ajustada se necessário
    print(f'{media_a:.2f}')

if __name__ == '__main__':
    main()

