temperatura = float(input("¿Qué temperatura hace? (ºC): "))
llueve = input("¿Llueve? (s/n): ").lower() == 's'

if temperatura < 10 and llueve:
    print("🧥☔ Lleva abrigo Y paraguas")
elif temperatura < 10:
    print("🧥 Hace frío, lleva abrigo")
elif llueve:
    print("☔ Lleva paraguas") 
else:
    print("😎 Solo camiseta")


