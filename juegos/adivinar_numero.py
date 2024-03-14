import random
def adivinar_numero():
    numero=random.randint(1, 10)
    print("Adivina numero del 1 al 10")
    adivinanza=int(input())
    if numero==adivinanza:
        return print("pass")
    else:
        return print("fail")