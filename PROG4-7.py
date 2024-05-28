diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#Crea una función en Python que calcule y devuelva el promedio de todas las
#notas de un estudiante dado,tomando como argumento el nombre del estudiante.

def promedios(nombre):
    # Verificar si el estudiante está en el diccionario
    if nombre in diccionario:
        # Obtener las notas del estudiante
        notas = diccionario[nombre].values()
        # Calcular el promedio de las notas
        promedio = sum(notas) / len(notas)
        return promedio
    else:
        return print("El estudiante",nombre," NO se encuentra en el diccionario.")

# Ejemplo de uso
nombre = input("Ingrese el nombre del estudiante: ")
promedio = promedios(nombre)
print("El promedio de las notas de" ,nombre," es:" ,promedio)