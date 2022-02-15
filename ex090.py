alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))

if alunos['media'] >= 6:
    alunos['status'] = 'Aprovado!'
else:
    alunos['status'] = 'Reprovado!'

print(f'Nome do aluno: {alunos["nome"]}')
print(f'A média do aluno é: {alunos["media"]}')
print(f'O status do aluno é {alunos["status"]}')



