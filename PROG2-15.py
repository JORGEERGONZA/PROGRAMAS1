#Escriba un programa para encontrar todas las raíces de una ecuación cuadrática
a=float(input("ingrese valor del coeficiente a\n"))
b=float(input("ingrese valor del coeficiente b\n"))
c=float(input("ingrese valor del coeficiente c\n"))
print("El valor del coeficiente a es de" ,a)
print("El valor del coeficiente b es de" ,b)
print("El valor del coeficiente c es de" ,c)
d=b**2-4*a*c
demas=d**(1/2)
demen=-d**(1/2)
x1=-(b+demas)/(2*a)
x2=-(b+demen)/(2*a)
print("EL VALOR DE LA 1RA RAIZ ES DE:" ,x1)
print("EL VALOR DE LA 2DA RAIZ ES DE:" ,x2)