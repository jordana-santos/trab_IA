import heapq

# ====================
# GRAFOS FIXOS
# ====================

inicio = 'RS'
objetivo = 'AM'

grafo = {
    'AC': {'RO': 2, 'AM': 5},
    'AM': {'RR': 4, 'PA': 10, 'AC': 5, 'RO': 4, 'MT': 6},
    'RO': {'AC': 2, 'MT': 5, 'AM': 4},
    'RR': {'AM': 4, 'PA': 6},
    'PA': {'AM': 5, 'RR': 6, 'MA': 6, 'TO': 5, 'AP': 1},
    'AP': {'PA': 1},
    'TO': {'PA': 5, 'MA': 3, 'PI': 6, 'GO': 5, 'MT': 5, 'BA': 6},
    'MA': {'PA': 6, 'TO': 3, 'PI': 3},
    'PI': {'TO': 6, 'MA': 3, 'CE': 2, 'BA': 5, 'PE': 3},
    'CE': {'PI': 2, 'RN': 1, 'PB': 2, 'PE': 1},
    'RN': {'CE': 1, 'PB': 1},
    'PB': {'RN': 1, 'CE': 2, 'PE': 1},
    'PE': {'PB': 1, 'AL': 1, 'BA': 4, 'PI': 3, 'CE': 1},
    'AL': {'PE': 1, 'SE': 1, 'BA': 4},
    'SE': {'AL': 1, 'BA': 3},
    'BA': {'SE': 3, 'PI': 5, 'GO': 6, 'MG': 6, 'ES': 4, 'TO': 6, 'PE': 4, 'AL': 4},
    'GO': {'TO': 5, 'BA': 6, 'MT': 4, 'MS': 3, 'DF': 1},
    'MT': {'RO': 5, 'TO': 5, 'GO': 4, 'DF': 6, 'MS': 4, 'AM': 6},
    'MS': {'GO': 3, 'MG': 6, 'MT': 4, 'SP': 5, 'PR': 4},
    'SP': {'MS': 5, 'MG': 3, 'RJ': 2, 'PR': 2},
    'MG': {'SP': 3, 'RJ': 2, 'ES': 2, 'BA': 6, 'MS': 6, 'GO': 5},
    'RJ': {'SP': 2, 'MG': 2, 'ES': 3},
    'ES': {'MG': 2, 'RJ': 3, 'BA': 4},
    'PR': {'SP': 2, 'SC': 1, 'MS': 4},
    'SC': {'PR': 1, 'RS': 3},
    'RS': {'SC': 3},
}

tempo_real = {
    'AC': {'RO': 3, 'AM': 6},
    'AM': {'RR': 5, 'PA': 12, 'AC': 6, 'RO': 5, 'MT': 7},
    'RO': {'AC': 3, 'MT': 6, 'AM': 5},
    'RR': {'AM': 5, 'PA': 7},
    'PA': {'AM': 6, 'RR': 7, 'MA': 7, 'TO': 6, 'AP': 2},
    'AP': {'PA': 2},
    'TO': {'PA': 6, 'MA': 4, 'PI': 7, 'GO': 6, 'MT': 6, 'BA': 7},
    'MA': {'PA': 7, 'TO': 4, 'PI': 4},
    'PI': {'TO': 7, 'MA': 4, 'CE': 3, 'BA': 6, 'PE': 4},
    'CE': {'PI': 3, 'RN': 2, 'PB': 3, 'PE': 2},
    'RN': {'CE': 2, 'PB': 2},
    'PB': {'RN': 2, 'CE': 3, 'PE': 2},
    'PE': {'PB': 2, 'AL': 2, 'BA': 5, 'PI': 4, 'CE': 2},
    'AL': {'PE': 2, 'SE': 2, 'BA': 5},
    'SE': {'AL': 2, 'BA': 4},
    'BA': {'SE': 4, 'PI': 6, 'GO': 7, 'MG': 7, 'ES': 5, 'TO': 7, 'PE': 5, 'AL': 5},
    'GO': {'TO': 6, 'BA': 7, 'MT': 5, 'MS': 4, 'DF': 2},
    'MT': {'RO': 6, 'TO': 6, 'GO': 5, 'DF': 7, 'MS': 5, 'AM': 7},
    'MS': {'GO': 4, 'MG': 7, 'MT': 5, 'SP': 6, 'PR': 5},
    'SP': {'MS': 6, 'MG': 4, 'RJ': 3, 'PR': 3},
    'MG': {'SP': 4, 'RJ': 3, 'ES': 3, 'BA': 7, 'MS': 7, 'GO': 6},
    'RJ': {'SP': 3, 'MG': 3, 'ES': 4},
    'ES': {'MG': 3, 'RJ': 4, 'BA': 5},
    'PR': {'SP': 3, 'SC': 2, 'MS': 5},
    'SC': {'PR': 2, 'RS': 4},
    'RS': {'SC': 4},
}

#perigo real g(n)
perigo_real = {
   'AC': {'RO': 4, 'AM': 3},
    'AM': {'RR': 5, 'PA': 6, 'AC': 3, 'RO': 4, 'MT': 7},
    'RO': {'AC': 4, 'MT': 6, 'AM': 4},
    'RR': {'AM': 5, 'PA': 7},
    'PA': {'AM': 6, 'RR': 7, 'MA': 8, 'TO': 9, 'AP': 5},
    'AP': {'PA': 5},
    'TO': {'PA': 9, 'MA': 8, 'PI': 10, 'GO': 11, 'MT': 10, 'BA': 12},
    'MA': {'PA': 8, 'TO': 8, 'PI': 9},
    'PI': {'TO': 10, 'MA': 9, 'CE': 11, 'BA': 12, 'PE': 13},
    'CE': {'PI': 11, 'RN': 12, 'PB': 13, 'PE': 13},
    'RN': {'CE': 12, 'PB': 13},
    'PB': {'RN': 13, 'CE': 13, 'PE': 14},
    'PE': {'PB': 14, 'AL': 13, 'BA': 12, 'PI': 13, 'CE': 13},
    'AL': {'PE': 13, 'SE': 12, 'BA': 11},
    'SE': {'AL': 12, 'BA': 11},
    'BA': {'SE': 11, 'PI': 12, 'GO': 11, 'MG': 10, 'ES': 9, 'TO': 12, 'PE': 12, 'AL': 11},
    'GO': {'TO': 11, 'BA': 11, 'MT': 10, 'MS': 10, 'DF': 9},
    'MT': {'RO': 6, 'TO': 10, 'GO': 10, 'DF': 9, 'MS': 9, 'AM': 7},
    'MS': {'GO': 10, 'MG': 10, 'MT': 9, 'SP': 12, 'PR': 13},
    'SP': {'MS': 12, 'MG': 11, 'RJ': 10, 'PR': 13},
    'MG': {'SP': 11, 'RJ': 9, 'ES': 8, 'BA': 10, 'MS': 10, 'GO': 10},
    'RJ': {'SP': 10, 'MG': 9, 'ES': 8},
    'ES': {'MG': 8, 'RJ': 8, 'BA': 9},
    'PR': {'SP': 13, 'SC': 10, 'MS': 13},
    'SC': {'PR': 10, 'RS': 9},
    'RS': {'SC': 9},
}

#distâncias estimadas h(n)
distancia_estimada = {
    'AC': 3,
    'AL': 10,
    'AP': 5,
    'AM': 0,
    'BA': 9,
    'CE': 10,
    'ES': 12,
    'GO': 8,
    'MA': 7,
    'MT': 6,
    'MS': 11,
    'MG': 11,
    'PA': 5,
    'PB': 12,
    'PR': 15,
    'PE': 11,
    'PI': 8,
    'RJ': 13,
    'RN': 12,
    'RS': 18,
    'RO': 2,
    'RR': 3,
    'SC': 16,
    'SP': 14,
    'SE': 11,
    'TO': 7
}

tempo_estimado = {
    'AC': 2,
    'AL': 9,
    'AP': 6,
    'AM': 0,
    'BA': 8,
    'CE': 8,
    'DF': 6,
    'ES': 9,
    'GO': 6,
    'MA': 6,
    'MT': 4,
    'MS': 6,
    'MG': 8,
    'PA': 4,
    'PB': 9,
    'PE': 9,
    'PI': 7,
    'PR': 9,
    'RJ': 9,
    'RN': 9,
    'RO': 3,
    'RR': 2,
    'RS': 10,
    'SC': 9,
    'SE': 9,
    'SP': 8,
    'TO': 5,
}

perigo_estimado = {
    'AC': 3,
    'AL': 13,
    'AP': 5,
    'AM': 0,
    'BA': 12,
    'CE': 13,
    'ES': 14,
    'GO': 10,
    'MA': 8,
    'MT': 12,
    'MS': 11,
    'MG': 13,
    'PA': 5,
    'PB': 15,
    'PR': 15,
    'PE': 14,
    'PI': 11,
    'RJ': 16,
    'RN': 16,
    'RS': 17,
    'RO': 4,
    'RR': 3,
    'SC': 15,
    'SP': 14,
    'SE': 13,
    'TO': 8
}


# ====================
# FUNÇÕES AUXILIARES
# ====================

def inicializar_open_set(inicio):
    """Cria a fila de prioridade inicial."""
    return [(0, inicio, [inicio], 0)]


def obter_heuristica(vizinho, distancia_estimada, tempo_estimado, perigo_estimado, peso_dist, peso_temp, peso_peri):
    """Calcula a heurística ponderada."""
    h_dist = distancia_estimada.get(vizinho, 0)
    h_temp = tempo_estimado.get(vizinho, 0)
    h_peri = perigo_estimado.get(vizinho, 0)
    return (peso_dist * h_dist) + (peso_temp * h_temp) + (peso_peri * h_peri)


def calcular_custo(atual, vizinho, grafo, tempo_real, perigo_real, peso_dist, peso_temp, peso_peri):
    """Calcula o custo real ponderado entre dois nós."""
    custo_dist = grafo[atual][vizinho]
    custo_temp = tempo_real[atual][vizinho]
    custo_peri = perigo_real[atual][vizinho]
    return (peso_dist * custo_dist) + (peso_temp * custo_temp) + (peso_peri * custo_peri)



def expandir_vizinhos(atual, caminho, g_total, grafo, tempo_real, perigo_real, distancia_estimada, tempo_estimado, perigo_estimado, peso_dist, peso_temp, peso_peri, menor_custo):
    """Gera a lista de vizinhos a serem adicionados à fila de prioridade."""
    vizinhos_expandidos = []

    for vizinho in grafo.get(atual, {}):
        if vizinho in caminho:
            continue

        custo = calcular_custo(atual, vizinho, grafo, tempo_real, perigo_real, peso_dist, peso_temp, peso_peri)
        novo_g = g_total + custo
        heuristica = obter_heuristica(vizinho, distancia_estimada, tempo_estimado, perigo_estimado, peso_dist, peso_temp, peso_peri)
        f_novo = novo_g + heuristica

        if novo_g <= menor_custo:
            vizinhos_expandidos.append((f_novo, vizinho, caminho + [vizinho], novo_g))

    return vizinhos_expandidos


def atualizar_melhores_caminhos(caminho, g_total, menor_custo, melhores_caminhos):
    """Atualiza a lista dos melhores caminhos."""
    if g_total < menor_custo:
        return g_total, [caminho]
    elif g_total == menor_custo:
        melhores_caminhos.append(caminho)
    return menor_custo, melhores_caminhos


# ====================
# A* PRINCIPAL
# ====================

def a_estrela_ponderada(inicio, objetivo, grafo, tempo_real, perigo_real, distancia_estimada, tempo_estimado, perigo_estimado, peso_dist, peso_temp, peso_peri):
    open_set = inicializar_open_set(inicio)
    heapq.heapify(open_set)
    closed_set = set()

    melhores_caminhos = []
    menor_custo = float('inf')

    while open_set:
        f_atual, atual, caminho, g_total = heapq.heappop(open_set)
        closed_set.add(atual)

        print(f"\n📍 Visitando: {atual}")
        print("OPEN:", [n for _, n, _, _ in open_set])
        print("CLOSED:", list(closed_set))

        if atual == objetivo:
            menor_custo, melhores_caminhos = atualizar_melhores_caminhos(
                caminho, g_total, menor_custo, melhores_caminhos
            )
            continue

        vizinhos = expandir_vizinhos(
            atual, caminho, g_total,
            grafo, tempo_real, perigo_real,
            distancia_estimada, tempo_estimado, perigo_estimado,
            peso_dist, peso_temp, peso_peri,
            menor_custo
        )

        for vizinho_info in vizinhos:
            heapq.heappush(open_set, vizinho_info)

    return melhores_caminhos, menor_custo


# ====================
# EXECUÇÃO
# ====================

if __name__ == "__main__":
    print("A* NA MIGRAÇÃO DE AVES")
    print("Escolha os pesos de distância, tempo e perigo.\nEles devem somar 1")
    try:
        peso_dist = float(input("Digite o peso da DISTÂNCIA (de 0 a 1): "))
        peso_temp = float(input("Digite o peso do TEMPO (de 0 a 1): "))
        peso_peri = float(input("Digite o peso do PERIGO (de 0 a 1): "))

        caminhos, custo = a_estrela_ponderada(
            inicio, objetivo,
            grafo, tempo_real, perigo_real,
            distancia_estimada, tempo_estimado, perigo_estimado,
            peso_dist, peso_temp, peso_peri
        )

        print("\nCaminhos ótimos encontrados:")
        for c in caminhos:
            print("→", " → ".join(c))
        print("Custo total mínimo (ponderado):", round(custo, 2))

    except ValueError as e:
        print("❌ Erro:", e)
