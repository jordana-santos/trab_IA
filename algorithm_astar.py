# distâncias reais g(n)
grafo = {
    'AC': {'RO': 3, 'AM': 4},
    'AL': {'PE': 2, 'SE': 1, 'BA': 3},
    'AM': {'RR': 5, 'PA': 7, 'AC': 4, 'RO': 4, 'MT': 8},
    'AP': {'PA': 3},
    'BA': {'SE': 3, 'PI': 5, 'GO': 5, 'MG': 4, 'ES': 4, 'TO': 6, 'PE': 4, 'AL': 3},
    'CE': {'PI': 3, 'RN': 1, 'PB': 2, 'PE': 2},
    'ES': {'MG': 2, 'RJ': 2, 'BA': 4},
    'GO': {'TO': 5, 'BA': 5, 'MT': 3, 'MS': 5, 'MG': 4},
    'MA': {'PA': 4, 'TO': 4, 'PI': 3},
    'MG': {'SP': 4, 'RJ': 2, 'ES': 2, 'BA': 4, 'MS': 6, 'GO': 4},
    'MT': {'RO': 5, 'TO': 5, 'GO': 3, 'MS': 6, 'AM': 8, 'PA': 7},
    'MS': {'GO': 5, 'MG': 6, 'MT': 6, 'SP': 5, 'PR': 4},
    'PA': {'AM': 7, 'RR': 6, 'MA': 4, 'TO': 5, 'AP': 3, 'MT': 7},
    'PB': {'RN': 1, 'CE': 2, 'PE': 1},
    'PE': {'PB': 1, 'AL': 2, 'BA': 4, 'PI': 3, 'CE': 2},
    'PI': {'TO': 6, 'MA': 3, 'CE': 3, 'BA': 5, 'PE': 3},
    'PR': {'SP': 3, 'SC': 2, 'MS': 4},
    'RJ': {'SP': 4, 'MG': 2, 'ES': 2},
    'RO': {'AC': 3, 'MT': 5, 'AM': 4},
    'RN': {'CE': 1, 'PB': 1},
    'RR': {'AM': 5, 'PA': 6},
    'RS': {'SC': 3},
    'SE': {'AL': 1, 'BA': 3},
    'SC': {'PR': 2, 'RS': 3},
    'SP': {'MS': 5, 'MG': 4, 'RJ': 4, 'PR': 3},
    'TO': {'PA': 5, 'MA': 4, 'PI': 6, 'GO': 5, 'MT': 5, 'BA': 6}
}

#distâncias estimadas h(n)
distancia_amazonas = {
    'AC': 3,
    'AL': 17,
    'AP': 8,
    'AM': 0,
    'BA': 14,
    'CE': 15,
    'ES': 15,
    'GO': 10,
    'MA': 9,
    'MT': 6,
    'MS': 12,
    'MG': 13,
    'PA': 5,
    'PB': 17,
    'PR': 16,
    'PE': 15,
    'PI': 12,
    'RJ': 14,
    'RN': 16,
    'RS': 20,
    'RO': 3,
    'RR': 3,
    'SC': 18,
    'SP': 17,
    'SE': 16,
    'TO': 10
}

#tempo real g(n)
tempo = {
    'AC': {'RO': 3, 'AM': 6},
    'AL': {'PE': 1, 'SE': 1, 'BA': 5},
    'AM': {'RR': 5, 'PA': 13, 'AC': 6, 'RO': 5, 'MT': 8},
    'AP': {'PA': 1},
    'BA': {'SE': 4, 'PI': 6, 'GO': 8, 'MG': 8, 'ES': 5, 'TO': 8, 'PE': 5, 'AL': 5},
    'CE': {'PI': 3, 'RN': 1, 'PB': 3, 'PE': 1},
    'ES': {'MG': 3, 'RJ': 4, 'BA': 5},
    'GO': {'TO': 6, 'BA': 8, 'MT': 5, 'MS': 4},
    'MA': {'PA': 8, 'TO': 4, 'PI': 4},
    'MG': {'SP': 4, 'RJ': 3, 'ES': 3, 'BA': 8, 'MS': 8, 'GO': 6},
    'MS': {'GO': 4, 'MG': 8, 'MT': 5, 'SP': 6, 'PR': 5},
    'MT': {'RO': 6, 'TO': 6, 'GO': 5, 'MS': 5, 'AM': 8},
    'PA': {'AM': 6, 'RR': 8, 'MA': 8, 'TO': 6, 'AP': 1},
    'PB': {'RN': 1, 'CE': 3, 'PE': 1},
    'PE': {'PB': 1, 'AL': 1, 'BA': 5, 'PI': 4, 'CE': 1},
    'PI': {'TO': 8, 'MA': 4, 'CE': 3, 'BA': 6, 'PE': 4},
    'PR': {'SP': 3, 'SC': 1, 'MS': 5},
    'RJ': {'SP': 3, 'MG': 3, 'ES': 4},
    'RN': {'CE': 1, 'PB': 1},
    'RO': {'AC': 3, 'MT': 6, 'AM': 5},
    'RR': {'AM': 5, 'PA': 8},
    'RS': {'SC': 4}
    'SE': {'AL': 1, 'BA': 4},
    'SC': {'PR': 1, 'RS': 4},
    'SP': {'MS': 6, 'MG': 4, 'RJ': 3, 'PR': 3},
    'TO': {'PA': 6, 'MA': 4, 'PI': 8, 'GO': 6, 'MT': 6, 'BA': 8},
}


#tempo estimado h(n)
tempo_amazonas = {
    'AC': 2,
    'AL': 9,
    'AP': 6,
    'AM': 0,
    'BA': 8,
    'CE': 8,
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


#perigo real g(n)
perigo = {
    'AC': {'RO': 4, 'AM': 3},
    'AL': {'PE': 13, 'SE': 12, 'BA': 11},
    'AM': {'RR': 5, 'PA': 6, 'AC': 3, 'RO': 4, 'MT': 7},
    'AP': {'PA': 5},
    'BA': {'SE': 11, 'PI': 12, 'GO': 11, 'MG': 10, 'ES': 9, 'TO': 12, 'PE': 12, 'AL': 11},
    'CE': {'PI': 11, 'RN': 12, 'PB': 13, 'PE': 13},
    'ES': {'MG': 8, 'RJ': 8, 'BA': 9},
    'GO': {'TO': 11, 'BA': 11, 'MT': 10, 'MS': 10},
    'MA': {'PA': 8, 'TO': 8, 'PI': 9},
    'MG': {'SP': 11, 'RJ': 9, 'ES': 8, 'BA': 10, 'MS': 10, 'GO': 10},
    'MS': {'GO': 10, 'MG': 10, 'MT': 9, 'SP': 12, 'PR': 13},
    'MT': {'RO': 6, 'TO': 10, 'GO': 10, 'MS': 9, 'AM': 7},
    'PA': {'AM': 6, 'RR': 7, 'MA': 8, 'TO': 9, 'AP': 5},
    'PB': {'RN': 13, 'CE': 13, 'PE': 14},
    'PE': {'PB': 14, 'AL': 13, 'BA': 12, 'PI': 13, 'CE': 13},
    'PI': {'TO': 10, 'MA': 9, 'CE': 11, 'BA': 12, 'PE': 13},
    'PR': {'SP': 13, 'SC': 10, 'MS': 13},
    'RJ': {'SP': 10, 'MG': 9, 'ES': 8},
    'RN': {'CE': 12, 'PB': 13},
    'RO': {'AC': 4, 'MT': 6, 'AM': 4},
    'RR': {'AM': 5, 'PA': 7},
    'RS': {'SC': 9}
    'SE': {'AL': 12, 'BA': 11},
    'SC': {'PR': 10, 'RS': 9},
    'SP': {'MS': 12, 'MG': 11, 'RJ': 10, 'PR': 13},
    'TO': {'PA': 9, 'MA': 8, 'PI': 10, 'GO': 11, 'MT': 10, 'BA': 12},
}


#perigo estimado até amazonas h(n)
perigo_amazonas = {
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


def personalizar_caminho():
    peso_tempo = float(input('Qual a importância do tempo passado em cada estado? (0 a 1):'))
    peso_perigo = float(input('Qual a importância do perigo que cada estado representa? (0 a 1):'))


def main():
    personalizar_caminho()

if __name__ == "__main__":
    main()
