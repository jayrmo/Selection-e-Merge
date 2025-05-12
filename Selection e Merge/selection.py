def selection_sort(lista):
    tamanho_lista = len(lista)
    comparacoes = 0

     # Loop externo para cada elemento da lista que queremos preencher
    for i in range(tamanho_lista - 1):
        menor_index = i # Marcamos o índice do menor elemento como o índice atual (vai ser trocado depois)

        # Olhar o resto da lista para confirmar se o menor elemento está na posição correta
        for j in range(i + 1, tamanho_lista):
            comparacoes += 1
            if lista[j] < lista[menor_index]:
                menor_index = j # Trocamos o índice do menor elemento para o índice atual já que ele é menor
        

        # Se o menor elemento encontrado não estiver já na posição 'i', realiza a troca.
        if menor_index != i:
            # Troca os elementos de lugar, o menor elemento vai para a posição 'i'
            # e o elemento que estava na posição 'i' vai para a posição do menor elemento
            lista[i], lista[menor_index] = lista[menor_index], lista[i]
    return lista, comparacoes
