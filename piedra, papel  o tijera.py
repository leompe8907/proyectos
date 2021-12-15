import random
condiciones = False
print("elija una opcion entre piedra - papel - tijera")
opcion1 = input("con cual opcion quieres jugar: ")

if opcion1 != "piedra" or opcion1 != "papel" or opcion1 != "tijera":
    condiciones = True
    
while condiciones:
    print("elija solo una de las tres opcion entre piedra - papel - tijera")
    opcion1 = input("con cual opcion quieres jugar: ")
    if opcion1 == "piedra" or opcion1 == "papel" or opcion1 == "tijera":
        condiciones = False
        
maquina = random.choice(["piedra","papel","tijera"])
print(f"la maquina jugo con: {maquina}")

if opcion1 == maquina:
    print("fue un empate")

if opcion1 == "piedra":
    if maquina == "papel":
        print("ganador la maquina")
    elif maquina == "tijera":
        print("ganador usuario")

if opcion1 == "papel":
    if maquina == "tijera":
        print("ganador la maquina")
    elif maquina == "piedra":
        print("ganador usuario")

if opcion1 == "tijera":
    if maquina == "piedra":
        print("ganador la maquina")
    elif maquina == "papel":
        print("ganador usuario")