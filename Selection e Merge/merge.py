def merge_sort(lista):
    tamanho = len(lista)
    comparacoes = 0

    # Verificar se a lista tem mais de um elemento (usado para acabar com a recursão)
    # Se a lista tiver 1 ou 0 elementos, já está ordenada
    if tamanho <= 1:
        return list(lista), 0
    
    meio = tamanho // 2

    # Dividir a lista em duas metades, criando uma cópia de cada uma para evitar modificar a principal
    esquerda = list(lista[:meio])
    direita = list(lista[meio:])

    # Ordenar cada metade usando recursão
    esquerda_ordenada, comparacoes_esquerda = merge_sort(esquerda)
    direita_ordenada, comparacoes_direita = merge_sort(direita)

    # Somar as comparações feitas nas duas metades
    comparacoes += comparacoes_esquerda + comparacoes_direita

    # Combinar as duas metades ordenadas usando a função merge
    lista_ordenada, comparacoes_merge = merge(esquerda_ordenada, direita_ordenada)
    comparacoes += comparacoes_merge

    return lista_ordenada, comparacoes


# Função auxiliar para combinar as duas listas ordenadas que a função merge_sort retorna
def merge(esquerda, direita):
    lista_ordenada = []
    comparacoes = 0

    index_esquerda = 0
    index_direita = 0
    tamanho_esquerda = len(esquerda)
    tamanho_direita = len(direita)

    # Enquanto houver elementos em ambas as listas
    while index_esquerda < tamanho_esquerda and index_direita < tamanho_direita:

        # Pega os elementos atuais de cada lista
        elemento_esquerda = esquerda[index_esquerda]
        elemento_direita = direita[index_direita]
        comparacoes += 1

        if elemento_esquerda <= elemento_direita:
            # O da esquerda é menor, adicionamos à lista ordenada
            lista_ordenada.append(elemento_esquerda)
            index_esquerda += 1 # Passa para o próximo elemento da lista esquerda

        else:
            # O da direita é menor, adicionamos à lista ordenada
            lista_ordenada.append(elemento_direita)
            index_direita += 1

    # Adiciona os elementos restantes da lista esquerda, se houver
    # (Isso só acontece se o loop 'while' parou porque index_direita >= tamanho_direita)
    if index_esquerda < tamanho_esquerda:
        lista_ordenada.extend(esquerda[index_esquerda:])

    # Adiciona os elementos restantes da lista direita, se houver
    if index_direita < tamanho_direita:
        lista_ordenada.extend(direita[index_direita:])
    
    return lista_ordenada, comparacoes
