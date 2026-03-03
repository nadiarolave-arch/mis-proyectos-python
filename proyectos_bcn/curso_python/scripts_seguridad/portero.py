nombre = input("Dime tu nombre: ")
pais = input("Dime tu pais: ")

if pais.lower() in ["españa", "spain", "espana"]:
    print("ACCESO DENEGADO: Ubicacion bloqueada.")
elif nombre.lower() == "felix":
    print("Hola Felix. Reconocido como usuario VIP.")
else:
    print(f"Bienvenido {nombre}, acceso concedido desde {pais}.")

