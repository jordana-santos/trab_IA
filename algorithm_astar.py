# distâncias reais g(n)
grafo = {
    'AC': [('RO', 2), ('AM', 5)],
    'AM': [('RR', 4), ('PA', 10), ('AC', 5), ('RO', 4), ('MT', 6)],
    'RO': [('AC', 2), ('MT', 5), ('AM', 4)],
    'RR': [('AM', 4), ('PA', 6)],
    'PA': [('AM', 5), ('RR', 6), ('MA', 6), ('TO', 5), ('AP', 1)],
    'AP': [('PA', 1)],
    'TO': [('PA', 5), ('MA', 3), ('PI', 6), ('GO', 5), ('MT', 5), ('BA', 6)],
    'MA': [('PA', 6), ('TO', 3), ('PI', 3)],
    'PI': [('TO', 6), ('MA', 3), ('CE', 2), ('BA', 5), ('PE', 3)],
    'CE': [('PI', 2), ('RN', 1), ('PB', 2), ('PE', 1)],
    'RN': [('CE', 1), ('PB', 1)],
    'PB': [('RN', 1), ('CE', 2), ('PE', 1)],
    'PE': [('PB', 1), ('AL', 1), ('BA', 4), ('PI', 3), ('CE', 1)],
    'AL': [('PE', 1), ('SE', 1), ('BA', 4)],
    'SE': [('AL', 1), ('BA', 3)],
    'BA': [('SE', 3), ('PI', 5), ('GO', 6), ('MG', 6), ('ES', 4), ('TO', 6), ('PE', 4), ('AL', 4)],
    'GO': [('TO', 5), ('BA', 6), ('MT', 4), ('MS', 3), ('DF', 1)],
    'MT': [('RO', 5), ('TO', 5), ('GO', 4), ('DF', 6), ('MS', 4), ('AM', 6)],
    'MS': [('GO', 3), ('MG', 6), ('MT', 4), ('SP', 5), ('PR', 4)],
    'SP': [('MS', 5), ('MG', 3), ('RJ', 2), ('PR', 2)],
    'MG': [('SP', 3), ('RJ', 2), ('ES', 2), ('BA', 6), ('MS', 6), ('GO', 5)],
    'RJ': [('SP', 2), ('MG', 2), ('ES', 3)],
    'ES': [('MG', 2), ('RJ', 3), ('BA', 4)],
    'PR': [('SP', 2), ('SC', 1), ('MS', 4)],
    'SC': [('PR', 1), ('RS', 3)],
    'RS': [('SC', 3)],
}

#distâncias estimadas h(n)
distancia_amazonas = {
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

#tempo real g(n)
tempo = {
    'AC': 2,
    'AL': 1,
    'AP': 2,
    'AM': 10,
    'BA': 5,
    'CE': 2,
    'ES': 1,
    'GO': 4,
    'MA': 4,
    'MT': 7,
    'MS': 4,
    'MG': 6,
    'PA': 9,
    'PB': 1,
    'PR': 2,
    'PE': 1,
    'PI': 3,
    'RJ': 1,
    'RN': 1,
    'RS': 3,
    'RO': 2,
    'RR': 2,
    'SC': 1,
    'SP': 3,
    'SE': 1,
    'TO': 3
}

#tempo estimado h(n)
tempo_amazonas = {
    'AC': 2,
    'AL': 1,
    'AP': 2,
    'AM': 10,
    'BA': 5,
    'CE': 2,
    'ES': 1,
    'GO': 4,
    'MA': 4,
    'MT': 7,
    'MS': 4,
    'MG': 6,
    'PA': 9,
    'PB': 1,
    'PR': 2,
    'PE': 1,
    'PI': 3,
    'RJ': 1,
    'RN': 1,
    'RS': 3,
    'RO': 2,
    'RR': 2,
    'SC': 1,
    'SP': 3,
    'SE': 1,
    'TO': 3
}

#perigo real g(n)
perigo = {
    'AC': ,
    'AL': ,
    'AP': ,
    'AM': ,
    'BA': ,
    'CE': ,
    'ES': ,
    'GO': ,
    'MA': ,
    'MT': ,
    'MS': ,
    'MG': ,
    'PA': ,
    'PB': ,
    'PR': ,
    'PE': ,
    'PI': ,
    'RJ': 500,  # passarinho pode ser baleado
    'RN': ,
    'RS': ,
    'RO': ,
    'RR': ,
    'SC': ,
    'SP': ,
    'SE': ,
    'TO': 
}

#perigo estimado até amazonas h(n)
perigo_amazonas = {
    'AC': ,
    'AL': ,
    'AP': ,
    'AM': ,
    'BA': ,
    'CE': ,
    'ES': ,
    'GO': ,
    'MA': ,
    'MT': ,
    'MS': ,
    'MG': ,
    'PA': ,
    'PB': ,
    'PR': ,
    'PE': ,
    'PI': ,
    'RJ': 500,  # passarinho pode ser baleado
    'RN': ,
    'RS': ,
    'RO': ,
    'RR': ,
    'SC': ,
    'SP': ,
    'SE': ,
    'TO': 
}

def personalizar_caminho():
    peso_tempo = float(input('Qual a importância do tempo passado em cada estado? (0 a 1):'))
    peso_perigo = float(input('Qual a importância do perigo que cada estado representa? (0 a 1):'))


def main():
    personalizar_caminho()

if __name__ == "__main__":
    main()
