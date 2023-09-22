#A função booleana atribui 'True' aos números ímpares
def f_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False


def main():
    #Entrada do número
    numero = float(input(""))

    #Exibe na tela a função 'f_iompar'
    print(f_impar(numero))


if __name__ == '__main__':
    main()
