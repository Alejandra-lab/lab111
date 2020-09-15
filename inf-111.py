print('TIEMPO DADO')

x= (int(input('x=')))

z=(int(input('segundos=')))

m=(int(input(('minutos=')))*60)

h=(int(input(('horas=')))*3600)

 
r= (z+m+h)

if  ( x >= r ):  
    print('la tarea estara a tiempo')
else:
    print('la tarea estara a destiempo')

print('fin del programa')

