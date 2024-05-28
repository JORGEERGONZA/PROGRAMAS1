diccionario = {
    "Alondra": {"Regresion": 3.4, "InteligenciaArtificial": 2.8},
    "Baltasar": {"Calculo": 2.0, "Probabilidad": 4.0},
    "Celestino": {"Bioestadistica": 1.0},
    "Doroteo": {"Programacion": 1.5, "Probabilidad": 2.5, "Bayesiana": 3.0},
    "Esperancita": {"Programacion": 1.0},
    "Fabiola": {"Multivariante": 3.2, "Probabilidad": 4.1, "HistoriaEst": 2.9}
}

#Si intentas acceder a una clave que no existe en el diccionario, como
#diccionario['Alondra']['Estadística']`,¿Qué ocurre y cómo puedes manejarlo?
if 'Estadística'in diccionario ['Alondra']:
    print(diccionario['Alondra']['Estadística'])
else:
    print("La clave 'Estadística' NO existe para 'Alondra'")