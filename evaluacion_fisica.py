
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese sus edad: "))
peso = int(input("Ingrese su peso en Kg: "))
horas = int(input("Ingrese sus horas de ejercicio a la semana: "))

calorias = horas * 350
if edad < 18:
    categoria = "juvenil"
else:
    categoria = "Adulto"

if horas >= 3:
    estado = "Fisicamente activo"
else:
    estado = "Requiere mayor actividad fisica"

print("--- RESUMEN DE EVALUACIÓN FÍSICA ---")
print(f"Nombre: {nombre}")
print(f"Calorías estimadas por semana: {calorias}")
print(f"Categoría: {categoria}")
print(f"Estado: {estado}")