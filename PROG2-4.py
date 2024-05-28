#Escriba un programa para verificar si un número es divisible o no por 5 y 11
x= float(input("Ingrese cualquier numero \n"))
if x%5==0 and x%11==0:
    print("EL NUMERO", x ,"ES DIVISBLE POR 5 Y 11")
else:
    print("EL NUMERO", x ,"NO ES DIVISBLE POR 5 Y 11")