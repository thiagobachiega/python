times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
         'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos')

print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os 4 ultimos colocados são: {times[6:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
print(f'O Palmeiras está em {times.index("Palmeiras")+ 1}º lugar!')