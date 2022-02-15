nome = input('Digite seu nome: ').strip().lower()
print(f'Seu nome contem {nome.count("a")} letras A')
print(f'A primeira letra A aparece na posição: {nome.find("a")+1}')
print(f'A ultima letra A aparece na posição: {nome.rfind("a")+1}')






