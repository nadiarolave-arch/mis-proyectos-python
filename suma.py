total = 0

while True:
    num = input("Número (o 's' para parar): ")
    if num == 's':
        break
    total += int(num)
    print(f"Total ahora: {total}")

print(f"Suma final: {total}")


