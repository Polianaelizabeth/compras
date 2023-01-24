desconto = 0

codigo = int(input("digite o codigo: "))
quantidade = int(input("digite a quantidade: "))

if 1 <= codigo <= 10:
    precoUn = float(10.0)
    precoTotal = precoUn * quantidade
    if precoTotal < 250:
        desconto = 0.05 * precoTotal
    precoFinal = precoTotal - desconto
elif 11 <= codigo <= 20:
    precoUn = float(15.0)
    precoTotal = precoUn * quantidade
    if 250 < precoTotal < 500:
        desconto = 0.1 * precoTotal
    precoFinal = precoTotal - desconto
elif 21 <= codigo <= 30:
    precoUn = float(20.0)
    precoTotal = precoUn * quantidade
    if 50 < precoTotal:
        desconto = 0.15 * precoTotal
    precoFinal = precoTotal - desconto
else:
    precoUn = float(30.0)
    precoTotal = precoUn * quantidade
    precoFinal = precoTotal
print("Preço unitário: ", precoUn, "preço total: ", precoTotal, "desconto: ", desconto, "preço final: ", precoFinal)
