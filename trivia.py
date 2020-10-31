#juego trivia hecho por mayu xD
print('¡hola! te invito a jugar mi juego trivia, trataremos temas como termux xd y entre otras cosas')
n1 = input('\n por favor dime como te llamas:')
print('\nmucho gusto', n1, ',empecemos')
puntaje = 0
print('me puedes decir con que comando en linux puedo listar la informacion de un directorio?')
print('a)cd')
print('b) ls')
print('c) cat')
print('d) mv')
print('e) rm')
respuesta_1 = input('\n tu respuesta: ')
while respuesta_1 not in ('a', 'b', 'c', 'd', 'e'): 
    respuesta_1 = input("debes volver a ingresar tu respuesta:")
if respuesta_1 == "b":
  puntaje += 10
  print("Muy bien", n1, "!")
else:
  puntaje -= 5
  print("Incorrecto", n1, "!")
    
print('\nsiguiente pregunta')
print('\ncual de estos comandos sirve para mover un archivo en termux')
print('a) cd')
print('b) cp')
print('c) mv')
print('d) cat')
print('e) chmod')
respuesta_2 = input('tu respuesta: ')
while respuesta_2 not in ('a', 'b', 'c', 'd', 'e'): 
    respuesta_2 = input("debes volver a ingresar tu respuesta:")
if respuesta_2 == "b":
   puntaje -= 5
   print('incorrecto', n1, '!')
elif respuesta_2 == "a":
   puntaje -= 5
   print('mal', n1, ', incorreto')
elif respuesta_2 == "d":
   puntaje -= 5
   print('no', n1, '! incorrecto')
elif respuesta_2 == "e":
   puntaje -= 5
   print('mal', n1, '! incorrecto')
else:
    puntaje += 10
    print('correcto', n1, '!!!!')


  
print('\nsiguiente pregunta')
print('\nque comando puede dar permisos?')
print('a) chmod')
print('b) cal')
print('c) rm')
print('d) mkdir')
print('e) ls -l')
respuesta_3 = input('\n tu respuesta: ')
while respuesta_3 not in ('a', 'b', 'c', 'd', 'e'): 
    respuesta_3 = input("debes volver a ingresar tu respuesta:")
if respuesta_3 == "a":
  puntaje += 10
  print("Muy bien", n1, "!")
else:
  puntaje -= 5
  print("Incorrecto", n1, "!")

print('\nsiguiente pregunta')
print('\ncual de estos comandos puede crear un directorio?')
print('a) rm')
print('b) mv')
print('c) cp')
print('d) mkdir')
print('e) exit')

respuesta_4 = input('\n tu respuesta: ')
while respuesta_4 not in ('a', 'b', 'c', 'd', 'e'): 
    respuesta_4 = input("debes volver a ingresar tu respuesta:")
if respuesta_4 == "d":
  puntaje += 10
  print("Muy bien", n1, "!")
else:
  puntaje -= 5
  print("Incorrecto", n1, "!")

print('\nsiguiente pregunta')
print('\ncon que comando puedo dar permisos e almacenaminto a termux?')
print('a) pwd')
print('b) ls -a')
print('c) lstree')
print('d) temux setup-storage')
print('e) rm -rf')

respuesta_5 = input('\n tu respuesta: ')
while respuesta_5 not in ('a', 'b', 'c', 'd', 'e'): 
    respuesta_5 = input("debes volver a ingresar tu respuesta:")
if respuesta_5 == "d":
  puntaje += 10
  print("Muy bien", n1, "!")
else:
  puntaje -= 5

print("Incorrecto", n1, "!")
print('\ngracias por jugar', n1, '!')
print('\neste es tu puntaje:')
print('tienes', puntaje , 'puntos')
print('\nchao, chuidate xd')