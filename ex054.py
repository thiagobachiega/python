from datetime import date

data = int(date.today().year)
maiores = 0
menores = 0

for c in range(1, 8):
    nascimento = int(input(f'Informe a data de nascimento da {c}º pessoa: '))
    if data - nascimento >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f'há {menores} de menores e {maiores} de maiores')


