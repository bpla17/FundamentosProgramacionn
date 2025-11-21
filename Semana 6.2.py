print("Ejercicios diccionarios - martes")
print("\nEjercicio 1 \n")
#Escribe tus datos
usuario = {
    "nombre": "Bruno",
    "edad": 18,
    "ciudad": "Monterrey"
}

print("Diccionario completo:")
print(usuario)
#Otra forma de mostrar el diccionario
print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Ciudad:", usuario["ciudad"])



print ("\nEjercicio 2\n")
videojuego = {
    "título": "Fortnite",
    "plataforma": "PC"
}
print ("Diccionario original:")
print(videojuego)
# Agregar nuevos datos
videojuego["año"] = 2017
videojuego[ "género"] = "Shooter"
videojuego["es_multijugador"] = True
print( "\nDiccionario después de agregar datos:")
print (videojuego)
print("\nNuevos datos agregados:")
print ("Año:", videojuego["año"])
print ("Género:", videojuego[ "género"])
print("¿Es multijugador?:", videojuego["es_multijugador"])



print("\nEjercicio 3\n")
#Agrega tus datos 
perfil = {
    "usuario": "Tu nombre",
    "seguidores": 14000,
    "publicaciones": 50,
    "ciudad": "Tu ciudad"
}
print("Perfil original:")
print (perfil)
print ("Seguidores antes:", perfil["seguidores"])
# Modificar valores (gana más seguidores)
perfil["seguidores"] = 5012051
perfil ["publicaciones"] = 456
print("\nPerfil actualizado:")
print(perfil)
print("Seguidores ahora:", perfil[ "seguidores"])
print("Publicaciones ahora:", perfil ["publicaciones"])



print("\nEjercicio 4 - eliminar un par clave-valor\n")
#Escribe tus datos
cuenta = {
    "usuario": "pon tu usuario",
    "email": "agrega tu email",
    "teléfono": "escribe tu numero",
    "ciudad": "pon tu cd"
}
print("Cuenta original (con teléfono): ")
print (cuenta)
# Eliminar el número de teléfono por privacidad
del cuenta[ "teléfono"]
print("\ncuenta después de eliminar teléfono:")
print(cuenta)
print("\nverificación - ¿existe 'teléfono'?:", "teléfono" in cuenta)



print( "\nEjercicio 5 - len\n")
#Agrega vuestra propia peli 
película = {
    "título": "Real Steel",
    "director": "Shawn Levy",
    "año": 2011,
    "género": "Ciencia Ficción",
    "duración_minutos": 127,
    "calificación": 10.0
}
print("Película:")
print (película)
cantidad = len(película)
print("\n¿Cuántos datos tiene el diccionario?:", cantidad)
print("El diccionario tiene", cantidad, "pares clave-valor")



print("\nEjercicio 6 - obtener las keys\n")
#Agrega vuestra cancion fav 
canción = {
    "titulo": "Amor Tumbado",
    "artista": "Natanael Cano",
    "album": "Mi Nuevo Yo",
    "año": 2019,
    "género": "Corrido Tumbado",
    "duración segundos": 221
}
print("Diccionario de canción:")
print (canción)
print("\nTodas las claves del diccionario:")
claves = canción.keys()
print(claves)
print("\nMostrando claves una por una:")
for clave in claves:
    print("-", clave)



print("InEjercicio 7: obtener los values")
calificaciones = {
    "Economia": 9.0,
    "Derecho de aduanas": 9.1,
    "Admin de negocios": 9.3,
    "Logistica y cadena de suministro": 9.7,
    "Mercadotecnia Internacional": 9.5
}
print("Diccionario de calificaciones:")
print(calificaciones)
print("\nTodos los valores del diccionario:")
valores = calificaciones.values()
print (valores)
print("\nMostrando valores uno por uno:")
for valor in valores:
    print("-", valor)
print("\nPromedio de calificaciones:", sum(valores) / len(valores))