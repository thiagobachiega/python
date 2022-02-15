import random

print('JOKENPO!'
      'Escolha:'
      '[0]Pedra '
      '[1]Papel '
      '[2]Tesoura ')

itens = ('Pedra', 'Papel', 'Tesoura')

escolha = int(input())


escolhapc = random.randint(0, 2)

print(f'O computador escolheu {itens[escolhapc]}, você escolheu {itens[escolha]}')

if escolha == escolhapc:
    print('EMPATE')
elif escolha == 0:
    if escolhapc == 1:
        print('Você perdeu!')
    elif escolhapc == 2:
        print('Você venceu!')

elif escolha == 1:
    if escolhapc == 0:
        print('Você venceu!')
    elif escolhapc == 2:
        print('Você perdeu!')

elif escolha == 2:
    if escolhapc == 0:
        print('Você perdeu!')
    elif escolhapc == 1:
        print('Você venceu!')

else:
    print('Jogada invalida')




