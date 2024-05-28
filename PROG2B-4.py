#Escriba un programa para mostrar el patrón como un triángulo rectángulo
#con un número.
filas = int(input("Ingrese el número de filas: \n"))

for i in range(1, filas + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()  