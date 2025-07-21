import random

def guess_the_number():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 3
    print("Olá, Adivinhe o Número...")
    print(f"Estou pensando em um número entre 1 e 100. Você tem {limite_tentativas} tentativas.")

    while tentativas < limite_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo. Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto. Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Número inválido, digite novamente")

    if palpite != numero_secreto:
        print(f"Você perdeu! O número era {numero_secreto}.")

guess_the_number()
