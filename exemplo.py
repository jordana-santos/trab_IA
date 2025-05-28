import heapq

inicio = 'A'
objetivo = 'D'

# Grafo com custos reais
grafo = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}

# Heurísticas até o objetivo
h_estimada = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
tempo_estimado = {'A': 12, 'B': 10, 'C': 5, 'D': 0}
tempo_real = {
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('B', 'C'): 2,
    ('B', 'D'): 8,
    ('C', 'D'): 3
}

def a_estrela_todos(grafo, h_estimada, tempo_real, tempo_estimado):
    open_set = []
    heapq.heappush(open_set, (0, inicio, [inicio], 0))  # (f, nó, caminho, g_total)
    closed_set = set()

    melhores_caminhos = []
    menor_custo = float('inf')

    while open_set:
        f_atual, atual, caminho, g_total = heapq.heappop(open_set)
        closed_set.add(atual)

        print(f"\n📍 Visitando: {atual}")
        print("🔓 OPEN:", [n for _, n, _, _ in open_set])
        print("🔒 CLOSED:", list(closed_set))

        if atual == objetivo:
            if g_total < menor_custo:
                menor_custo = g_total
                melhores_caminhos = [caminho]
            elif g_total == menor_custo:
                melhores_caminhos.append(caminho)
            continue  # não para aqui, continua buscando outros caminhos

        for vizinho, custo in grafo[atual].items():
            if vizinho in caminho:  # evitar ciclos
                continue
            tempo = tempo_real.get((atual, vizinho), 0)
            novo_g = g_total + custo + tempo
            heuristica = h_estimada[vizinho] + tempo_estimado[vizinho]
            f_novo = novo_g + heuristica

            if novo_g <= menor_custo:  # só considera caminhos com chance de serem ótimos
                heapq.heappush(open_set, (f_novo, vizinho, caminho + [vizinho], novo_g))

    return melhores_caminhos, menor_custo

# EXECUÇÃO
caminhos, custo = a_estrela_todos(grafo, h_estimada, tempo_real, tempo_estimado)

# RESULTADO FINAL
print("\n✅ Caminhos ótimos encontrados:")
for c in caminhos:
    print("→", " → ".join(c))
print("💰 Custo total mínimo:", custo)
