#JOKENPO
from random import choice

jokenpo = ['Pedra', 'Papel', 'Tesoura']
sorteado = choice(jokenpo)
print('Vamos jogar JOKENPO?')
print('-'*30)
jogador = int(input('Digite 1 para PEDRA, 2 para PAPEL ou 3 para TESOURA: '))
if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
else:
    jogador = 'Tesoura'

print('-'*30)
if sorteado == jogador:
    print(f'Tente de novo. {sorteado} é igual a {jogador}.')
elif (sorteado == 'Pedra' and jogador == 'Tesoura') or (sorteado == 'Papel' and jogador == 'Pedra') or (sorteado == 'Tesoura' and jogador == 'Papel'):
    print(f'Você perdeu. {sorteado} ganha de {jogador}.')
else:
    print(f'Parabéns, você ganhou! {jogador} ganha de {sorteado}.')
