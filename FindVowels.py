print('Questão 02; contagem de vogais')

p = input('Digite uma frase: ')
l = p.lower() 
s = 0  
a = e = i = o = u = 0

for k in list(l):
  if k in 'aáàãâeéèêiíìîoóòõôuúùû': # Contagem de vogais
    s += 1
  if k in 'aáâãà': # Contagem de A's
    a += 1
  if k in 'eéêè': # Contagem de E's
    e += 1    
  if k in 'iíîì': # Contagem de I's
    i += 1
  if k in 'oóôõò': # Contagem de O's
    o += 1
  if k in 'uúûù': # Contagem de U's
    u += 1

if s >= 1:
  print(f'No total há {s} vogais na entrada {p}.')
  print(f'Há {a} A`s, {e} E`s, {i} I`s, {o} O`s, {u} U`s')
else:
  print(f'Não há vogais na entrada {p}.')
  
input() #input para não fechar a execução do programa antes de ser concluído