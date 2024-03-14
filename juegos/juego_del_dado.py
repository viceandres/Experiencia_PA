import random
def juego_del_dado():
    p_hombre=0
    p_pc=0
    while p_hombre<30 or p_pc<30:
        input("Presiona Enter para lanzar el dado")
        numero=random.randint(1, 6)
        p_hombre+=numero
        print(" tu numero es "+str(numero)+" y tu puntuacion "+str(p_hombre))
        if p_hombre>=30:
            print("gana hombre")
            break
        numero=random.randint(1, 6)
        p_pc+=numero
        print(" el numero del pc es "+str(numero)+" y su puntuacion "+str(p_pc))
        if p_pc>=30:
            print("gana pc")
            break