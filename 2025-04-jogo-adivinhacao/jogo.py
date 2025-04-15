import random

print("🎲 Bem-vindo ao Jogo da Adivinhação!")
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        chute = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if chute == numero_secreto:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("🔼 O número é maior.")
        else:
            print("🔽 O número é menor.")
    except ValueError:
        print("❌ Por favor, digite apenas números inteiros.")

