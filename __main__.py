from classes import *


def main():
    obj_1 = Analise('Leitos_2026.csv')
    obj_2 = Consultas('Leitos_2026.csv')
    obj_1.grafico_leitos('BA')

if __name__ == '__main__':
    main()
