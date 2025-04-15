import random

print("Bem-vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 100)

tentativa = int(input("Digite um número entre 1 e 100: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou.")
else:
    print(f"Errou! O número era {numero_secreto}.")
