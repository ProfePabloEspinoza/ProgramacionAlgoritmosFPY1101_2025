c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
c6 = False
pw = input('Ingrese contraseña: ')

#condicion 1
if len(pw) >= 8 and len(pw) <= 16:
  c1 = True

#condicion 2, 3, 4 y 5
especial = 0
for c in pw:
  if c in '0123456789':
    c2 = True
  if c.lower() in 'abcdefghijklmnñopqrstuvwxyz':
    c3 = True
  if c in '-_*.!?#$%':
    especial = especial + 1
  if ' ' not in pw:
    c5 = True

if especial <= 1:
  c4 = True

# condicion 6
if pw[-1] not in '-_*.!?#$%':
  c6 = True

if c1 and c2 and c3 and c4 and c5 and c6:
  print('Contraseña válida.')
else:
  print('Contraseña inválida')