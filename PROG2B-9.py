#Escriba un programa que imprima los números primos hasta cierto número
def primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

m = int(input("Donde termina el rango: "))

for num in range(2,m):
    if primo(num):
        print(num)
  