hora_actual_str = input("Ingrese la hora actual (formato HH:MM): ") 

hora_actual_lista = hora_actual_str.split(":")
hora_actual = int(hora_actual_lista[0])
minutos_actual = int(hora_actual_lista[1])

horas_sumar = int(input("Ingrese el numero de horas a sumar:  "))

hora_futura = (hora_actual+horas_sumar) % 24

minutos_futuro = (minutos_actual+(horas_sumar*60)) % 60


print(f"la hora despues de {horas_sumar} sera: {hora_futura:02d}:{minutos_futuro:02d}")
