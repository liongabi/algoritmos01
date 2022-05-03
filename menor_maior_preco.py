precos= [1000000, 46000, 16000, 46000, 17000, 5000, 3500, 4785000]

atual = 0
maisBarato = precos[0]
maisCaro = precos[0]

for n in (precos):
    if n <= maisBarato:
        maisBarato = n

    if n >= maisCaro:
        maisCaro = n

    else:
        pass

print("\nO carro mais barato custa R${}.".format(maisBarato))
print("\nO carro mais cato custa R${}.".format(maisCaro))



