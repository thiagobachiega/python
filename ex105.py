def notas(* n, sit=True):
    '''
    A função notas serve para analisar a situação das notas dos alunos.
    :param n: Serve para informar as notas dos alunos (informe quantas precisar)
    :param sit: parametro opcional, serve para exibir a situação do aluno baseado no calculo da média: abaixo de 4.0 RUIM, entre 4.0 e 6.0 RECUPERAÇÃO e acima de 6.0 BOM.
    :return: Exibe o total de notas informadas, qual a maior e a menor nota, média e a situação do aluno(opcional).
    '''
    boletin = {}
    soma = 0
    for c in range(0, len(n)):
        soma = soma + n[c]
        if c == 0:
            maior = n[c]
            menor = n[c]
        elif n[c] > maior:
            maior = n[c]
        elif n[c] < menor:
            menor = n[c]
    media = soma / len(n)
    boletin['total'] = len(n)
    boletin['maior'] = maior
    boletin['menor'] = menor
    boletin['media'] = media
    if sit == True:
        if media < 4:
            boletin['situação'] = 'Ruim'
        elif media > 4 and media < 6:
            boletin['situação'] = 'Recuperação'
        else:
            boletin['situação'] = 'Bom'
    print(boletin)
def notasv2(*n, sit=True):
    boletin = {}
    boletin['total'] = len(n)
    boletin['maior'] = max(n)
    boletin['menor'] = min(n)
    boletin['media'] = sum(n) / len(n)
    if sit == True:
        if boletin['media'] < 4:
            boletin['situação'] = 'Ruim'
        elif boletin['media'] > 4 and boletin['media'] < 6:
            boletin['situação'] = 'Recuperação'
        else:
            boletin['situação'] = 'Bom'
    return boletin


resp = notasv2(8.0, 9.0, 8.5, 10, 6, 8, sit=True)
print(resp)
help(notas)
