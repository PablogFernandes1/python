n1 = float(input('what is the price of the product? R$'))
discount = n1 - (n1 * 5 / 100)

print('the product that cost R${}, in the promotion with a discount and 5% will cost R${}'.format(n1, discount))