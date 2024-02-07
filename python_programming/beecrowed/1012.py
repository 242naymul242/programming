values = input().split()
pi = 3.14159
a = float(values[0])
b = float(values[1])
c = float(values[2])
triangulo = 1/2 * a * c
print(f"TRIANGULO: {triangulo:.3f}")
circulo = pi * c**2
print(f"CIRCULO: {circulo:.3f}")
trapezio = 1/2 * ( a + b ) * c
print(f"TRAPEZIO: {trapezio:.3f}")
square = b * b
print(f"QUADRADO: {square:.3f}")
rectangle = a * b
print(f"RETANGULO: {rectangle:.3f}")