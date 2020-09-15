print('ECUACION DE 2DO GRADO')
a=  int(input('Variable1= '))

b=  int(input('Variable2= '))

c=  int(input('Variable3= '))

d= (b**2-4*a*c)

if d>0:
    print('hay dos raices reales distintas')
elif (d==0):
    print('hay dos raices iguales y reales')
else :
    print('tenemos raices imaginarias')

