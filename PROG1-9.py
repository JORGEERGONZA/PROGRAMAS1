#Determinar el pago mensual M de un pr ́estamo simple con capital P ,tasa de
#interes mensual r,y ńumero de pagos n.Formula aproximada:M = P r1−(1+r)−n
P= float(input("Ingrese el capital a depositar \n"))
r= float(input("Ingrese la tasa de interes mensual \n"))
n= float(input("Ingrese los numeros de pagos \n"))
M= (P*r)/(1-((1+r))**(-n))
print("EL VALOR DEL PAGO MENSUAL ES DE: ", M)