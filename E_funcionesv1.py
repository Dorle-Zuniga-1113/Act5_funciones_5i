print("manejo de funciones V1")
def hola_mundo():
    print("Hola, estoy aquí")
# llamando a la funcion 
hola_mundo()
def mensa(msg):
    print(msg)
def EscribeNC(nombre, apellido):
    print(nombre, apellido)
    print(f"tu nombre completo es {nombre} {apellido}")
def suma2numeros(n1,n2):
        s=n1+n2
        return f"la suma de {n1} y de {n2} es de: ",s 
# llamando a la función
mensa("el profe me sorprendio enviando mensajes") 
mensa("hola wazaaaaaaa")
EscribeNC("Dorle", "Zuñiga")
print("funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))