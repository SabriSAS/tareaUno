Monto = float(input("Digite el monto a invertir: "))

InteresAnual = 4

PrimerResultado = Monto * (InteresAnual / 100 + 1)
SegundoResultado = PrimerResultado * (InteresAnual / 100 + 1)
TercerResultado = SegundoResultado * (InteresAnual / 100 + 1)



print("Balance tras el primer año:" + str(round(PrimerResultado, 2)))

print("Balance tras el segundo año:" + str(round(SegundoResultado, 2)))

print("Balance tras el tercer año:" + str(round(TercerResultado, 2)))