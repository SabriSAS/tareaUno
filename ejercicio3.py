Monto = float(input("Cual es el monto a invertir: "))
InteresAnual = float(input("Cual es el interes anual: "))
Anios = int(input("A cuantos años desea invertir: "))

Resultado = Monto * (InteresAnual / 100 + 1) ** Anios

print("El capital obtenido es : " + str(Resultado))