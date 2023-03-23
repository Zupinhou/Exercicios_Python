def ler_produtos():
  produtos = []
  print('Digite os dados dos produtos (aperte enter duas vezes para escrever os códigos de busca):')
  while True:
    linha = input().strip()
    if not linha:
      break
    codigo, descricao, quantidade, preco = linha.split('#')
    produtos.append((codigo, descricao, int(quantidade), float(preco)))
  return produtos

def buscar_produto(codigo, produtos):
  for produto in produtos:
    if produto[0] == codigo:
      return produto
  return None

def imprimir_produto(produto, codigo):
  if produto is None:
    print(f"Código {codigo} não localizado na lista de produtos!")
  else:
    print(f"Produto Localizado: ({produto[0]}, {produto[1]}, {produto[2]}, {produto[3]})")

# Programa principal
produtos = ler_produtos()

print('Digite os códigos dos produtos a serem buscados:')
while True:
  codigo = input().strip()
  if not codigo:
    break
  produto = buscar_produto(codigo, produtos)
  imprimir_produto(produto, codigo)

print('Obrigado por utilizar nosso sistema!!!')

input() #input para não fechar a execução do programa antes de ser concluído