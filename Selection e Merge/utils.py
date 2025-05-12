import random
import time

def criar_lista_aleatoria(tamanho):
    lista = [random.randint(0, tamanho * 5) for _ in range(tamanho)]
    return lista

def medir_tempo_execucao(funcao, lista):
    lista_copia = list(lista)

    # Marca o tempo de início EXATAMENTE antes de chamar a função
    inicio = time.perf_counter()

    # Chama a função que é para ser medida
    lista_resultante, comparacoes = funcao(lista_copia)

    # Marca o tempo de fim EXATAMENTE depois que a função terminou
    fim = time.perf_counter()

    # Calcula o tempo decorrido em segundos
    tempo_execucao_segundos = fim - inicio
    return lista_resultante, comparacoes, tempo_execucao_segundos