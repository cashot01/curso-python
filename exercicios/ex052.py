# leia nº inteiro e fala se é numero primo ou não
num = int(input('nº: '))
tot = 0
for c in range(1, num +1):
   if num % c == 0:
     print('\033[32m', end='')
     tot += 1
   else:
      print('\033[31m', end='')
   print('{} '.format(c), end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
   print('nº primo')
else:
   print('NÃO PRIMO')
 