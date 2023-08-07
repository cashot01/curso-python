# leia em metros, converta em cm e mm
m = int(input('nº: '))
cm = m*100
mm = m*1000
print('{}{}{}m = {}{}{}cm = {}{}{}mm'.format('\033[1;35m', m ,'\033[m', '\033[1;35m', cm,'\033[m', '\033[1;35m', mm, '\033[m'))