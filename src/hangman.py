#Lista de palabras
palabras = ["Cafe","Taza","Manolo","popopo"]

#Seleccionamos una palabra al azar
i = random.randint(0,len(palabras)-1)
lista_caracteres = list(palabras[i])
print(lista_caracteres)

#Generamos lista guiones
lista_guiones = ["_"] * len(lista_caracteres)



vidas = 5 
while vidas > 0:
 print (lista_guiones)
 #Registramos el input y creamos una lista con las posiciones de la letra
 player_input = input()
 lista_posiciones = []

 
 #Saca las posiciones de las letras si coinciden
 for index,n in enumerate(lista_caracteres): 
  if player_input == n:
   lista_posiciones.append (index)
 #Si hay una letra correcta la sustituye
 for posicion in lista_posiciones:
    lista_guiones[posicion] = player_input
 
 print(f"¡Has introducido la {player_input}!")
 if player_input in lista_caracteres:
  print (f"{player_input} es correcta!")

 else: 
  vidas = vidas-1
  print (f"{player_input} no es correcta, te quedan {vidas} vidas") 
 if vidas == 0:
  print ("Has perdido")

   
 if lista_guiones == lista_caracteres:
  print("Has ganado!")
  break
  
#Quieres volver a jugar?