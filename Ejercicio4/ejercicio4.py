# ejemplo de un Menú

número = int(input("Menú: 1(ver números), 0(salir)"))
while número != 0:

    x = 0
    while x < 10:
     print("El valor de x es:",x)
     x += 1


    print("Saliendo,,,")
    número  = int(input("Menú: 1(ver números), 0(salir)"))
     
print("Muchas gracias")