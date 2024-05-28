#Dada una lista de números retornar el número menor y su posición en la lista
lista2=[8, 5, -11, 7, -4, 9 ]
menor=100
posicion=-1
for i in range(len(lista2)):
    
    if lista2[i]<menor:
        menor=lista2[i]
        posicion=i
 
print("EL MENOR ES",menor, "Y SU POSICION ES", posicion)