def voto(anon):
    import datetime
    data = datetime.date.today().year
    idade = data - anon
    if idade < 16:
        return f'Com {idade} anos não é possivel votar'
    elif idade > 65 or 16 <= idade < 18:
        return f'Com {idade} anos o voto é opcional!'
    else:
        return f'Com {idade} anos o voto é obrigatório!'


ano = int(input('Em que ano você nasceu?'))
print(voto(ano))
