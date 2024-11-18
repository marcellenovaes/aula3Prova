

# # Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# # Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# # À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave.
# # Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário.
# # Por fim, exiba o valor total da compra.

colunas ="-" * 60
print(colunas)
print("NOTA FISCAL MANUAL")
print(colunas)


dicionario = {}


def inserir_produtos ():
    chave = input("Digite o nome do produto: ")
    valor = float(input("Digite o preço do produto: R$"))
    dicionario[chave] = valor
    
    
for i in range(5):
    inserir_produtos()
    print(f"\n item {i+1}/5 adicionado!")


soma = sum(dicionario.values())
    
    
print(colunas)
print(f" TOTAL: R$ {soma}")
print("Volte sempre!")