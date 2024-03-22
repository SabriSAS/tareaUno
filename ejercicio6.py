CantidadBarra = int(input("Indique la cantidad de barras de pan no frescas: "))

PrecioNormal = 3.49 
Descuento = 60

PrecionDescuento = CantidadBarra * PrecioNormal * (1 - Descuento/100)

print("Precio Normal de cada barra: " + str(PrecioNormal) + "€")
print("Precio Normal de las barras vendidas: " + str(round(PrecioNormal*CantidadBarra,2)) + "€")
print("Descuento Total a aplicar: " + str(Descuento) + "%")
print("Precion Con Desuento de las barras vendidas: " + str(round(PrecionDescuento, 2)) + "€")