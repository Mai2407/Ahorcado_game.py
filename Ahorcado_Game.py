import time

nombre = input("Como te llemas? ")
print("Hola, "+nombre," Es hora de jugar el ahorcado")
print(" ")

time.sleep(1)

print("Comienza a adivinar")

time.sleep(0.5)

palabra = "REPUBLICA DOMINICANA"
tupalabra = ""
vidas = 5

while vidas > 0:
   fallas = 0
   for letra in palabra:
     if letra in tupalabra:
       print(letra,end="")
     else:
        print("*",end="")
        fallas += 1

   if fallas == 0 :
     print("Ganaste................")
     break

   tuletra = input("Introduce una letra: ").upper()
   tupalabra += tuletra

   if tuletra not in palabra:
     vidas -= 1
     print("Equivocacion..........")
     print("Tu tienes ", +vidas, " vidas")
   if  vidas == 0:
     print("Perdiste...........")
else:
  print("Gracias por participar.........")







