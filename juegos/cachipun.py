import random

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    
    print('Elige Piedra, Papel o Tijera')

    eleccion_persona = input()
    eleccion_computador = random.choice(['Piedra', 'Papel', 'Tijera'])
    if eleccion_persona == eleccion_computador:
        print('Empate')
        return cachipun()
    if eleccion_persona == 'Tijera' and eleccion_computador == 'Papel':
        print('Gano la persona')
    if eleccion_persona == 'Papel' and eleccion_computador == 'Piedra':
        print('Gano la persona')
    if eleccion_persona == 'Piedra' and eleccion_computador == 'Tijera':
        print('Gano la persona')
    if eleccion_persona == 'Tijera' and eleccion_computador == 'Piedra':
        print('Gano la maquina')
    if eleccion_persona == 'Papel' and eleccion_computador == 'Tijera':
        print('Gano la maquina')
    if eleccion_persona == 'Piedra' and eleccion_computador == 'Papel':
        print('Gano la maquina')
    pass

cachipun()