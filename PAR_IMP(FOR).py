begin= int(input("Ingrese inicio rango"))
end= int(input("Ingrese final rango"))

contp=0
conti=0
for i in range(begin,end):
    impar=i%2
    if( impar==1):
        conti=conti+1
    else:
        contp=contp+1
        
print(contp,"PARES","-->",conti,"IMPARES")