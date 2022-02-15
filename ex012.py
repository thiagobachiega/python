preco = float(input('Qual o preço do produto?: '))
desconto = preco * 0.05
valor = preco - desconto
print('Promoção o produto de: {}R$ está saindo por apenas: {}R$'.format(preco, valor))

