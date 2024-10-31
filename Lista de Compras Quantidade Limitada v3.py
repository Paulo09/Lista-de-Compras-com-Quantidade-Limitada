# 1. Criar uma lista vazia para armazenar os itens de compras
lista_compras = []

# 2. Definir o limite de unidades
limite_total = 20
quantidade_total = 0

print("Bem-vindo à lista de compras! Adicione produtos até o limite de 20 unidades.")

# 3. Solicitar ao usuário que adicione itens à lista até que o limite seja atingido
while quantidade_total < limite_total:
    try:
        # Solicita o nome do produto
        produto = input("Digite o nome do produto: ")
        
        # Solicita a quantidade do produto
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        
        # Verifica se a quantidade é válida e não excede o limite restante
        if quantidade <= 0:
            print("A quantidade deve ser um número positivo.")
            continue
        
        if quantidade_total + quantidade > limite_total:
            print(f"Você excederia o limite total de 20 unidades. Você ainda pode adicionar até {limite_total - quantidade_total} unidades.")
            continue
        
        # 4. Adicionar o item à lista
        lista_compras.append({"produto": produto, "quantidade": quantidade})
        quantidade_total += quantidade
        
        print(f"{produto} (x{quantidade}) adicionado à lista!")
    
    # Tratar exceções para entradas inválidas
    except ValueError:
        print("Quantidade inválida! Por favor, insira um número inteiro.")

# 5. Exibir a lista final de compras
print("\nLista de compras final:")
for item in lista_compras:
    print(f"- {item['produto']}: {item['quantidade']} unidades")

print("Limite de unidades atingido!")
