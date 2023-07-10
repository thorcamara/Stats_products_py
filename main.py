total = totalProductsAbove1000 = cheapestProduct = count = 0
cheapestProductName = ''
while True:
    product = str(input('Name of the Product: '))
    price = float(input('Price: $ '))
    count += 1
    total += price
    if price > 1000:
        totalProductsAbove1000 += 1
    if count == 1 or price < cheapestProduct:
        cheapestProduct = price
        cheapestProductName = product
    answer = ' '
    while answer not in 'YN':
        answer = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if answer == 'N':
        break
print('{:-^40}'.format('\033[4;33mEND OF THE PROGRAM\033[m'))
print(f'The total of the purchase was \033[4;32m${total:.2f}\033[m')
print(f'We  have \033[4;32m{totalProductsAbove1000}\033[m products costing more than \033[4;32m$1000.00\033[m')
print(f'The cheapest product was \033[4;32m{cheapestProductName}\033[m costing \033[4;32m${cheapestProduct:.2f}\033[m')
