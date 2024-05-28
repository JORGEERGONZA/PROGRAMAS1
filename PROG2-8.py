#Escriba un programa para ingresar cualquier caracter y verifique si es
#vocal o consonante.
vocales = ['a','e','i','o','u','A','E','I','O','U']

s=input("Ingrese algun caracter \n")
caracter = s

if caracter in vocales:
    print("EL CARACTER ES UNA VOCAL")
else:
    print("EL CARACTER NO ES UNA VOCAL")