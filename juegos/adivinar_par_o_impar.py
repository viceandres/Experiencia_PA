import random
def adivinar_par_o_impar():
    print('elige una opción: par o impar')
    numero=random.randint(1,2)
    a=input()
    if (a=='par' and numero==1) or (a=='impar' and numero==2):
        print('perdiste loser')
    else:
        print('ganaste cr7 siuu')


adivinar_par_o_impar()

    #"""
   # Esta función representa el juego de adivinar si un número es par o impar.
   # Tienes que permitir que el usuario ingrese una de las dos opciones y
   # generar un número aleatorio para ver si es par o impar.
   # Se debe mostrar si el usuario adivina correctamente o no.