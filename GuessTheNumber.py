import random

def guess_the_number():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Olá, Adivinhe o Número...")
    print("Estou pensando em um número entre 1 e 100")

    while True:
        try:
            palpite = int(input("Seu palpite: "))
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

guess_the_number()
