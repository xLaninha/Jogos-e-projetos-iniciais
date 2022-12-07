#adivinhe o número
import random
def adivinhe(x):
    numero_qualquer = random.randint(1, x) 
    a = 0  
    print("Adivinhe o número que está entre 1 e", x)
    while a!=numero_qualquer:
        a = int(input("Qual o número?"))
        if a < numero_qualquer:
            print("Continue tentando! O número é maior que ", a)
        elif a > numero_qualquer:
            print("Quase lá! O número é um menor que ", a)
    print("Parabéns!!! Você adivinho o número. O número era ", numero_qualquer)

adivinhe(1000)