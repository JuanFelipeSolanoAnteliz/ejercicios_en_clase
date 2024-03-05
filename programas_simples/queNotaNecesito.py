c1 = float(input("Ingrese nota certamen 1:  "))
c2 = float(input("Ingrese nota certamen 2:  "))
Nl = float(input("Ingrese nota laboratorio :  "))

Nf = (c1 + c2)/3 * 0.7 + Nl * 0.3  
resta = (Nf-100) *(-1)

if Nf < 60:
    print(f"necesita nota de {resta} en el certamen 3 ")

    

