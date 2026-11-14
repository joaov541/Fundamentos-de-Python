#cabeçalho do programa
print()
print()
print("|*******************************|")
print("|       venda com reajuste      |")
print("|          VERSÃO 1.0           |")
print("|*******************************|")
print()
print()


precoCompra = float(input("Digite o preço de compra do produto: "))
percentualAplicado = float(input("Digite o percentual a ser aplicado: "))

# calcula o preço de venda e o exibe

precoVenda = precoCompra + ((precoCompra * percentualAplicado) / 100)

print(f"Preço de venda: R${precoVenda}")

if percentualAplicado < 50:
    print("Percentual inferior a 50 - o produto será vendido com margem pequena de lucro")