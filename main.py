import random

def computer_guess():
    low = 1
    high = 50
    feedback = ''
    print('****** JOGO DO NÚMERO SECRETO ****** \n')
    print('Imagine um número entre 1 e 50. O computador tentara acertá-lo')

    while feedback != 'C':
        if low != high:
            random_number = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'O número {random_number} é maior[H], menor[L] ou igual[C] ao seu número? ').upper()

        if feedback == 'H':
            high = random_number + 1
        elif feedback == 'L':
            low = random_number - 1

    print('Isso ai! O computador acertou o seu número :)')

computer_guess()





