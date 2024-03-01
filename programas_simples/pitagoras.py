import math
cat1 = float(input("ingrese el cateto 1: "))
cat2 = float(input("ingrese el cateto 2: "))

hipotenusa2 = cat1**2 + cat2**2 
hipotenusa = math.sqrt(hipotenusa2)
print(f"Lahipotenusa del triangulo evaluado es: {hipotenusa}.")