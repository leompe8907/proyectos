import random
import getpass

def juego(usuario1,usuario2):
    if((usuario1 == "piedra" and usuario2 == "tijera" or
        usuario1 == "tijera" and usuario2 == "papel" or
        usuario1 == "papel" and usuario2 == "piedra")):
        return True
    else:
        return False

def solo():

    condiciones = ""
    print("elija una opcion entre piedra - papel - tijera")
    usuario1 = input("con cual opcion quieres jugar: ").lower()

    if usuario1 == "piedra" or usuario1 == "papel" or usuario1 == "tijera":
        condiciones = False
    elif usuario1 != "piedra" or usuario1 != "papel" or usuario1 != "tijera":
        condiciones = True
        
    while condiciones:
        print("elija solo una de las tres opcion entre piedra - papel - tijera")
        usuario1 = input("con cual opcion quieres jugar: ").lower()
        if usuario1 == "piedra" or usuario1 == "papel" or usuario1 == "tijera":
            condiciones = False
            
    usuario2 = random.choice(["piedra","papel","tijera"])
    print(f"la maquina jugo con: {usuario2}")

    if usuario1 == usuario2:
        return("!fue un empate!")
    if juego(usuario1,usuario2):
        return "!felicidades haz ganado la partida!"
    else:
        return "!es una pena, perdiste!"
    
def pareja():
    condicion = ""
    nombre1 = input("porfavor escriba su nombre: ")
    jugador1 = getpass.getpass(f"{nombre1} elije entre piedra - papel - tijera ").lower()
    
    if jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera":
        condicion = False
    elif jugador1 != "piedra" or jugador1 != "papel" or jugador1 != "tijera":
        condicion = True
    while condicion:
        print("elija solo una de las tres opcion entre piedra - papel - tijera")
        jugador1 = input("con cual opcion quieres jugar: ").lower()
        if jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera":
            condicion = False
    
    nombre2 = input("porfavor escriba su nombre: ")
    jugador2 = getpass.getpass(f"{nombre2} elije entre piedra - papel - tijera ")
    
    if jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijera":
        condicion = False
    elif jugador2 != "piedra" or jugador2 != "papel" or jugador2 != "tijera":
        condicion = True
    while condicion:
        print("elija solo una de las tres opcion entre piedra - papel - tijera")
        jugador2 = input("con cual opcion quieres jugar: ").lower()
        if jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijera":
            condicion = False
    
    if jugador1 == jugador2:
        return("!fue un empate!")
    if juego(jugador1,jugador2):
        return f"!felicidades haz ganado la partida {nombre1} con {jugador1} !"
    else:
        return f"!felicidades haz ganado la partida {nombre2} con {jugador2} !"

print("-- Bienvendido como te gustaria jugar --")

print(". Solo")

print(". Pareja")

print(". Salir")

opcion = input("Indique lo que le gustaria hacer:").lower()

validar = ""

if opcion == "solo" or opcion == "pareja" or opcion == "salir":
    validar = False
elif opcion != "solo" or opcion != "pareja" or opcion != "salir":
    validar = True
    
while validar:
    print("Debes elegir entre las tres opciones")
    print(". Solo")
    print(". Pareja")
    print(". Salir")
    opcion=input("por favor indique cual de las tres opciones quiere hacer: ").lower()
    if opcion == "solo" or opcion == "pareja" or opcion == "salir":
        validar = False

if opcion == "solo":
    print(solo())
elif opcion == "pareja":
    print(pareja())
elif opcion == "salir":
    print("-- MUCHAS GRACIAS POR PARTICIPAR --")