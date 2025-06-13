def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

# Área cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
print("Área del cuadrado:", area_cuadrado(lado))

# Área triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
print("Área del triángulo:", area_triangulo(base, altura))

# Área rectángulo
base_r = float(input("Ingrese la base del rectángulo: "))
altura_r = float(input("Ingrese la altura del rectángulo: "))
print("Área del rectángulo:", area_rectangulo(base_r, altura_r))
