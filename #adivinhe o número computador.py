#adivinhe o número com usuário
import random 
def pc_adivinha(x):
    y = 1
    z = x
    fb = ""
    while fb != "c" and y != z+1:
        adivinha = random.randint(y,z+1)
        fb = input(f"O número {adivinha} é muito alto (a), muito baixo (b) ou correto (c)?")
        if fb == "a":
            z = adivinha -1 
        elif fb == "b":
            y = adivinha + 1
    print(f"Ihaaaa! O computador acertou! O número era {adivinha}!")

pc_adivinha(100)