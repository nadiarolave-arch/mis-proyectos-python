# Datos fijos para evitar fallos de teclado
tu_edad = 34
edad_felix = tu_edad + 1

print("--- PROYECTO BCN: RESULTADOS ---")
print(f"Tu edad: {tu_edad} años.")
print(f"La edad de Felix: {edad_felix} años.")

if tu_edad >= 18:
    print("Eres mayor de edad.")

# Cálculo del cumple de Felix (19 de Julio)
from datetime import date
hoy = date.today()
proximo = date(hoy.year, 7, 19)
if proximo < hoy:
    proximo = date(hoy.year + 1, 7, 19)

faltan = (proximo - hoy).days
print(f"Faltan {faltan} dias para el cumple de Felix.")


from datetime import date

# --- DATOS BASE ---
tu_edad = 34
edad_felix = tu_edad + 1
hoy = date.today()

# --- CÁLCULOS DE AÑOS ---
# Si hoy es 2026, calculamos el año de nacimiento aproximado
tu_anio = hoy.year - tu_edad
anio_felix = hoy.year - edad_felix

# --- LÓGICA DEL CUMPLE ---
dia_f, mes_f = 19, 7  # Felix: 19 de Julio
proximo = date(hoy.year, mes_f, dia_f)
if proximo < hoy:
    proximo = date(hoy.year + 1, mes_f, dia_f)
faltan = (proximo - hoy).days

# --- RESULTADOS ---
print(f"\n>>> REPORTE PROYECTO BCN <<<")
print(f"Tu naciste aprox. en {tu_anio} y tienes {tu_edad} años.")
print(f"Felix nacio en {anio_felix} (es un año mayor).")

# Verificación de Signo (Lógica Junior)
if mes_f == 7 and dia_f <= 22:
    print("Signo de Felix: Cancer (Confirmado).")

print(f"Faltan {faltan} dias para su proximo cumple.")

if faltan < 30:
    print("¡Ojo! Falta menos de un mes para el cumple.")
else:
    print("Aun tienes tiempo para el regalo.")


# --- GUARDAR EN ARCHIVO ---
with open("reporte_bcn.txt", "w") as archivo:
    archivo.write(f"Reporte de Felix y yo\n")
    archivo.write(f"Año Felix: {anio_felix}\n")
    archivo.write(f"Dias para el cumple: {faltan}\n")

print("\n[INFO] ¡Reporte guardado con exito en 'reporte_bcn.txt'!")

​<!-- end list -->



