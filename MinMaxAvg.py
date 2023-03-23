print('Questão 01; menor, maior e média')

ls_n = []
c = s = 0
l = input('Digite um número: ')

if l == '':
 print('Nenhum número foi lido - A primeira linha lida foi vazia')
else:
  n = int(l)
  ls_n.append(n)
  s += n
  c += 1
  while True:
    l = input('Digite um número: ')
    if l == '':
      break
    else:
      n = int(l)
      ls_n.append(n)
    c += 1
    s += n

if len(ls_n) != 0:
  print(f'O menor número é {min(ls_n)}, o maior número é {max(ls_n)} e a média é {(s / c):.2f}')

input() #input para não fechar a execução do programa antes de ser concluído
