#pedra papel tesoura
import random

def vitoria(j,c):
    if (j == 'p' and c == 'tesoura' ) or (j == 's' and c == 'pedra') or (j == 't' and c == 'papel'):
        return True

def partida():
    usuario = input("Pedra 'p', papel 's' ou tesoura 't'?")
    pc = random.choice(['pedra', 'papel', 'tesoura'])
    if usuario == pc:
        return "Empate!"
    if vitoria(usuario, pc):
        return f"Você ganhou! O computador escolheu {pc}"
    return f"Você perdeu! O computador escolheu {pc}"

partida()