import random

print("Bem-vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        tentativa = int(input("Digite um número entre 1 e 100: "))
        if tentativa < 1 or tentativa > 100:
            print("Por favor, digite um número dentro do intervalo de 1 a 100.")
            continue
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
            break
        elif tentativa < numero_secreto:
            print("O número é maior. Tente novamente!")
        else:
            print("O número é menor. Tente novamente!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
