import random
def memoria():
    frase=""
    for i in range(10):
        num=random.randint(0,9)
        frase+=str(num)
    print("recuerda la secuencia de numeros "+ frase)
    input("enter para jugar")
    for i in range(50):
        print("-")
    je=input("ahora dime la frase")
    if je==frase:
        return(print("GANASTEEEEE"))
    else:
        return(print("es dificil adivinar una secuencia de 5 numeros"))