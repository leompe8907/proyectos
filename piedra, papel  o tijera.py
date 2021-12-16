import random
import getpass

validar = ""

def juegosolo(opcion1,maquina):
    if((opcion1 == "piedra" and maquina == "tijera" or
        opcion1 == "tijera" and maquina == "papel" or
        opcion1 == "papel" and maquina == "piedra")):
        return True
    else:
        return False

def juegopareja(usuario1,usuario2):
    if((usuario1 == "piedra" and usuario2 == "tijera" or
        usuario1 == "tijera" and usuario2 == "papel" or
        usuario1 == "papel" and usuario2 == "piedra")):
        return True
    else:
        return False

def solo():

    condiciones = ""
    print("elija una opcion entre piedra - papel - tijera")
    opcion1 = input("con cual opcion quieres jugar: ").lower()

    if opcion1 == "piedra" or opcion1 == "papel" or opcion1 == "tijera":
        condiciones = False
    elif opcion1 != "piedra" or opcion1 != "papel" or opcion1 != "tijera":
        condiciones = True
        
    while condiciones:
        print("elija solo una de las tres opcion entre piedra - papel - tijera")
        opcion1 = input("con cual opcion quieres jugar: ").lower()
        if opcion1 == "piedra" or opcion1 == "papel" or opcion1 == "tijera":
            condiciones = False
            
    maquina = random.choice(["piedra","papel","tijera"])
    print(f"la maquina jugo con: {maquina}")

    if opcion1 == maquina:
        return("!fue un empate!")
    if juegosolo(opcion1,maquina):
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
    if juegopareja(jugador1,jugador2):
        return f"!felicidades haz ganado la partida {nombre1} !"
    else:
        return f"!felicidades haz ganado la partida {nombre2} !"

print("-- Bienvendido como te gustaria jugar --")
n = input("Indique lo que le gustaria hacer:").lower()

if n == "solo" or n == "pareja" or n == "salir":
    validar == False
elif n != "solo" or n != "pareja" or n != "salir":
    validar == True
while validar:
    print("Debes elegir entre las tres opciones")
    n=input(print("por favor indique cual de las tres opciones quiere hacer: ")).lower()
    if n == "solo" or n == "pareja" or n == "salir":
        validar == False

if n == "solo":
    print(solo())
elif n == "pareja":
    print(pareja())
elif n == "salir":
    print("-- MUCHAS GRACIAS POR PARTICIPAR --")