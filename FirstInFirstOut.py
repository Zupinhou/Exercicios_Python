def vetor_principal(n):
  vetor = []
  for i in range(n):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
    pessoa = (nome, idade, peso, altura)
    vetor.append(pessoa)
  return vetor

def alfabeticamente(vetor):
  primeiro_nome = vetor[0][0]
  for pessoa in sorted(vetor, key=lambda x: x[0]):
    if pessoa[0] >= primeiro_nome:
      print(f"('{pessoa[0]}', {pessoa[1]}, {pessoa[2]}, {pessoa[3]})")

def idadecrescente(vetor):
  primeira_idade = vetor[0][1]
  for pessoa in vetor:
    if pessoa[1] >= primeira_idade:
      print(f"('{pessoa[0]}', {pessoa[1]}, {pessoa[2]}, {pessoa[3]})")

def pesocrescente(vetor):
  primeiro_peso = vetor[0][2]
  for pessoa in vetor:
    if pessoa[2] >= primeiro_peso:
      print(f"('{pessoa[0]}', {pessoa[1]}, {pessoa[2]}, {pessoa[3]})")

def alturacrescente(vetor):
  primeira_altura = vetor[0][3]
  for pessoa in vetor:
    if pessoa[3] >= primeira_altura:
      print(f"('{pessoa[0]}', {pessoa[1]}, {pessoa[2]}, {pessoa[3]})")

# Programa principal

n = int(input("Digite a quantidade de pessoas a serem mantidas no vetor: "))
vetor = vetor_principal(n)

opcao = int(input('[0] Ordem alfabética\n[1] Ordem crescente de idade\n[2] Ordem crescente de peso\n[3] Ordem crescente de altura\nInsira o valor: '))

if opcao == 0:
  print('Dados das pessoas com nome(s) maiores que o primeiro:')
  alfabeticamente(vetor)
  print('Obrigado por utilizar nosso sistema!')
elif opcao == 1:
  print('Dados das pessoas com idade(s) maiores que o primeiro:')
  idadecrescente(vetor)
  print('Obrigado por utilizar nosso sistema!')
elif opcao == 2:
  print('Dados das pessoas com peso(s) maiores que o primeiro:')
  pesocrescente(vetor)
  print('Obrigado por utilizar nosso sistema!')
elif opcao == 3:
  print('Dados das pessoas com altura(s) maiores que o primeiro:')
  alturacrescente(vetor)
  print('Obrigado por utilizar nosso sistema!')
else:
  print("Opção inválida.")

input() #input para não fechar a execução do programa antes de ser concluído