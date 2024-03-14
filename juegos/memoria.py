import random
def memoria():
    frase=""
    for i in range(5):
        num=random.randint(0,9)
        frase+=str(num)
    je=input("adivina la secuencia de numeros/n")
    if je==frase:
        return(print("GANASTEEEEE"))
    else:
        return(print("es dificil adivinar una secuencia de 5 numeros"))