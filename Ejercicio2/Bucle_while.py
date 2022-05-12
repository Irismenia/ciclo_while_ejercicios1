# BUCLE WHILE

import math


número = int(input("Digite un número: "))

while número < 0:
    print("Error -> Debería ser un número positivo")
    número = int(input("Digite un número: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(número)):.2f}")