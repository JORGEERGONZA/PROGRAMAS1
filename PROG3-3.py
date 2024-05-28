#Dada una lista de números hallar la media
lista=[8, 5, -11, 7, -4, 9 ]
menor=0
for i in range(len(lista)):
    menor=menor+ lista[i]
    
print ("EL VALOR DE LA MEDIA ES DE:", menor/len(lista))