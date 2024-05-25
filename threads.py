from threading import Thread, Lock
import sys

soma = 0
lock = Lock()

def soma_numeros(numeros):
    """
    Função que soma os números de uma lista

    :param numeros: lista de números
    """
    global soma
    # Bloqueia a thread para que a soma seja feita de forma correta
    lock.acquire()
    soma += sum(numeros)
    lock.release()

if __name__ == '__main__':
    # Recebe o número de threads que serão utilizadas como argumento. Assim, o programa se adapta a qualquer número de threads
    n_threads = int(sys.argv[1])

    threads = []
    listas = []

    # Recebe os números que serão somados como input do usuário, transformando-os em uma lista de inteiros
    lista_numeros = [int(x) for x in input('Digite os números que deseja somar separados por espaço: ').split(' ')]

    # Divide a lista de números em n_threads listas. Assim, cada thread irá somar uma parte da lista. 
    # a divisão é feita pegando um número a cada n_threads números. Ex: n_threads = 2, lista = [1, 2, 3, 4, 5] -> listas = [[1, 3, 5], [2, 4]]
    for i in range(n_threads):
        listas.append(lista_numeros[i::n_threads])

    # Cria as threads com cada lista de números
    for i in range(n_threads):
        threads.append(Thread(target=soma_numeros, args=(listas[i],)))

    # Inicia as threads
    for thread in threads:
        thread.start()

    # Espera todas as threads terminarem. Assim, elas não serão executadas indefinidamente
    for thread in threads:
        thread.join()

    print(f'A soma dos números é: {soma}')

    