print("funciones creadas por el usuario")

def Mi_lista():
    print("LISTA")
    amigos=["homero","paty","lety"]
    for nava in amigos: 
        print(nava)
        #llamar a la función
Mi_lista()

def tuplas():
    print("TUPLAS")
    frutas = ("apple", "banana", "cherry")

    for a1 in frutas: 
        print(a1)

def dicci():
    print("DICCIONARIO")
    carro = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964


}
    for a2 in carro: 
        print(a2)
    

def conju():
    print("CONJUNTOS")
    ropa = {"camisa", "pants", "shorts"}
    for a3 in ropa: 
        print(a3)

dicci()
tuplas()
conju()
