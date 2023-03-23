# Define a classe para os objetos de produto
class Produto:
  def __init__(self, codigo, descricao, quantidade, preco):
    self.codigo = codigo
    self.descricao = descricao
    self.quantidade = quantidade
    self.preco = preco
  def __str__(self):
    return f'{self.codigo}#{self.descricao}#{self.quantidade}#{self.preco}'

# Subprograma para ler os dados dos produtos
def ler_produtos():
  produtos = []
  print('Digite os dados dos produtos (aperte enter duas vezes para escrever os códigos de busca):')
  while True:
    linha = input().strip()
    if not linha:
      break
    codigo, descricao, quantidade, preco = linha.split('#')
    produtos.append(Produto(codigo, descricao, int(quantidade), float(preco)))
  return produtos

# Subprograma para buscar um produto pelo código
def buscar_produto(codigo, produtos):
  for produto in produtos:
    if produto.codigo == codigo:
      return produto
  return None

# Subprograma para imprimir os dados de um produto
def imprimir_produto(produto):
  if produto is None:
    print(f"Código {codigo} não localizado na lista de produtos!")
  else:
    print(f"Produto Localizado: ({produto.codigo}, {produto.descricao}, {produto.quantidade}, {produto.preco})")

# Programa principal
produtos = ler_produtos()

print('Digite os códigos dos produtos a serem buscados:')
while True:
  codigo = input().strip()
  if not codigo:
    break
  produto = buscar_produto(codigo, produtos)
  imprimir_produto(produto)

input() #input para não fechar a execução do programa antes de ser concluído