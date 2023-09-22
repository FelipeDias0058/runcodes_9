#Exibe uma mensagem na tela de acordo com a cor
def f_semaforo(cor):
    if 'V' in cor:
        print("Siga")
    elif 'A' in cor:
        print("Atenção")
    elif 'E' in cor:
        print("Pare")
    else:
        print("Digite 'V', 'A' ou 'E'.")


def main():
    #Digita a cor do semáforo(V, A, E)
    cor = input("").upper()

    #Executa a função "f_semaforo"
    f_semaforo(cor)


if __name__ == '__main__':
    main()
