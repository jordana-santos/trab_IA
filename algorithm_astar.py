#matriz de adjacencias da academia, com distancias
grafo = {
    'Bicicleta': [('Supino', 5), ('C', 5)],
    'B': [('A', 2), ('D', 4)],
    'C': [('A', 5)],
    'D': [('B', 4)]
}

energia = {
    'Bicicleta': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

tempo = {
    'Bicicleta': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

def personalizar_caminho():
    estado_inicial = int(input('Qual é o seu estado inicial?'))
    estado_final = int(input('Qual estado deseja chegar?'))
    intensidade = float(input('Qual a intensidade do treino? \n0.5 = leve\n1 = moderado \n2 = intenso\n'))
    peso_distancia = float(input('Qual a importância da distância entre máquinas? (0 a 1):'))
    peso_energia = float(input('Qual a importância da energia gasta em cada exercício? (0 a 1):'))
    peso_tempo = float(input('Qual a importância do tempo de execução de um exercício? (0 a 1):'))


def main():
    personalizar_caminho()

if __name__ == "__main__":
    main()
