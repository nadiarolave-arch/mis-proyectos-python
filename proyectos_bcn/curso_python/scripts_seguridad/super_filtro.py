print("--- SISTEMA DE VIGILANCIA ACTIVO ---")

while True: # <--- Esta es la llave del bucle
    nombre = input("\nNombre (o escribe 'salir'): ")
    
    # Una forma de cerrar el programa con lógica
    if nombre.lower() == "salir":
        print("Cerrando sistema...")
        break # <--- Rompe el bucle y sale
        
    pais = input("País: ")
    edad = int(input("Edad: "))

    # Aquí sigue tu lógica de antes (con sangría/espacio)
    if pais.lower() in ["españa", "spain", "espana"]:
        print(">>> BLOQUEO: España no tiene acceso.")
    elif edad < 18:
        print(">>> BLOQUEO: Menor de edad.")
    else:
        print(f">>> BIENVENIDO, {nombre.upper()}.")




