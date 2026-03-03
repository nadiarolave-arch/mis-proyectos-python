numero_secreto = 7
intentos = 0

while True:
    guess = int(input("Adivina el número (1-10, 0=salir): "))
    intentos += 1
    
    if guess == 0:
        print("¡Adiós!")
        break
    elif guess < numero_secreto:
        print("📈 Más alto")
    elif guess > numero_secreto:
        print("📉 Más bajo")
    else:
        print(f"✅ ¡Correcto en {intentos} intentos!")
        break


