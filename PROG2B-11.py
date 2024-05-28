#Escriba un programa que dado un número imprima la suma de sus dígitos
# Solicitar al usuario que ingrese un número
numero = input("Ingrese un número: ")
suma = 0

for digito in numero:
    suma= suma+int(digito)
print("LA SUMA DE SUS DIGITOS ES DE: ",suma)