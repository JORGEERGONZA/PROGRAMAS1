def celsius_a_fah(c):
    f=(1.8*c)+32
    return f

celsius=float(input("INGRESE TEMPERATURA"))
print("TEMPERATURA GRINGA:",celsius_a_fah(celsius))