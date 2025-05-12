import selection
import merge
import utils
import matplotlib.pyplot as plt
import numpy as np



print("--- Comparando Algoritmos de Ordenação ---")

tamanhos_teste = [10, 100, 500, 1000] # Pequena, Média, Grande, Maior
comparacoes_s = []
comparacoes_m = []
tempo_s = []
tempo_m = []
# Loop para cada tamanho de lista que vai ser testado
for tamanho in tamanhos_teste:
    print("\n--- Testando com lista de tamanho {} ---".format(tamanho))
    lista_aleatoria = utils.criar_lista_aleatoria(tamanho)

    print("Teste com Selection Sort:")
    try:
        lista_ordenada_selection, comparacoes_selection, tempo_execucao_selection = utils.medir_tempo_execucao(selection.selection_sort, lista_aleatoria)
        # print("Lista ordenada (primeiros 10 elementos):", lista_ordenada_selection[:10])
        print("Comparações:", comparacoes_selection)
        print("Tempo de execução (s):", tempo_execucao_selection)
        comparacoes_s.append(comparacoes_selection)
        tempo_s.append(tempo_execucao_selection)
        
    except Exception as e:
        print("Ocorreu algum erro:", e)

    print("Teste com Merge Sort:")
    try:
        lista_ordenada_merge, comparacoes_merge, tempo_execucao_merge = utils.medir_tempo_execucao(merge.merge_sort, lista_aleatoria)
        # print("Lista ordenada (primeiros 10 elementos):", lista_ordenada_merge[:10])
        print("Comparações:", comparacoes_merge)
        print("Tempo de execução (s):", tempo_execucao_merge)
        comparacoes_m.append(comparacoes_merge) 
        tempo_m.append(tempo_execucao_merge)
    except Exception as e:
        print("Ocorreu algum erro:", e)
    
    
    
    
print("\n--- Fim dos Testes ---")





# # Criando subplots
# fig, ax1 = plt.subplots()

# # Gráfico de comparações
# ax1.plot(tamanhos_teste, comparacoes_s, label='Selection Sort - Comparações', marker='o')
# ax1.plot(tamanhos_teste, comparacoes_m, label='Merge Sort - Comparações', marker='o')
# ax1.set_xlabel('Tamanho da lista')
# ax1.set_ylabel('Número de Comparações')
# ax1.legend(loc='upper left')

# # Segundo eixo para tempo
# ax2 = ax1.twinx()
# ax2.plot(tamanhos_teste, tempo_s, label='Selection Sort - Tempo (s)', marker='s', linestyle='--')
# ax2.plot(tamanhos_teste, tempo_m, label='Merge Sort - Tempo (s)', marker='s', linestyle='--')
# ax2.set_ylabel('Tempo de execução (s)')
# ax2.legend(loc='upper right')


# plt.title('Comparação entre Selection Sort e Merge Sort')
# plt.grid(True)
# plt.show()






n = len(tamanhos_teste)
index = np.arange(n)
bar_width = 0.35

# Criando o gráfico com barras para comparações
fig, ax = plt.subplots(figsize=(10,6))

# Barras para Selection Sort e Merge Sort
ax.bar(index - bar_width/2, comparacoes_s, bar_width, label='Selection Sort - Comparações')
ax.bar(index + bar_width/2, comparacoes_m, bar_width, label='Merge Sort - Comparações')

# Argumentos adicionais
ax.set_xlabel('Tamanho da lista')
ax.set_ylabel('Número de Comparações')
ax.set_xticks(index)
ax.set_xticklabels(tamanhos_teste)

# Criando e ajustando o segundo eixo para o tempo
ax2 = ax.twinx()
ax2.set_ylabel('Tempo de execução (s)')
# ax2.set_ylim(ax.get_ylim())  # Manter escala consistente para o tempo
ax2.plot(index, tempo_s, color='orange', marker='o', linestyle='-', linewidth=2, label='Tempo (s) - Selection Sort')
ax2.plot(index, tempo_m, color='green', marker='s', linestyle='-', linewidth=2, label='Tempo (s) - Merge Sort')

# Inserir legenda consolidada
lines_labels = [ax.get_legend_handles_labels(), ax2.get_legend_handles_labels()]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax.legend(lines, labels, loc='upper left', bbox_to_anchor=(1.05, 1), fontsize='small')

plt.title('Comparação Selection Sort vs Merge Sort')
plt.tight_layout()
plt.show()