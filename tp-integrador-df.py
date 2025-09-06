import pandas as pd #importa pandas para manejo de datos

def registrar_visitas():  # Función para registrar visitas
    datos = {"Nombre": [], "Edad": [], "Curso": [], "Motivo": []} # Diccionario para almacenar datos
    for i in range(4):
        print(f"\nRegistro #{i+1}")
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad: "))
        curso = input("Curso: ")
        motivo = input("Motivo de la visita: ")
        datos["Nombre"].append(nombre)
        datos["Edad"].append(edad)
        datos["Curso"].append(curso)
        datos["Motivo"].append(motivo)
    df = pd.DataFrame(datos) # Crea DataFrame
    df.to_csv("visitas_makerspace.csv", index=False)  # Guarda en CSV
    return df 

def mostrar_datos(): # Función para mostrar datos
    df = pd.read_csv("visitas_makerspace.csv")  # Lee desde CSV
    print("\n--- Lista de estudiantes que ingresaron a la MakerSpace ---")
    print(df)

    print("\n--- Cantidad de visitas por curso ---")
    print(df["Curso"].value_counts())

    print("\nPrimer estudiante que ingresó a la MakerSpace:")
    print(df.iloc[0]["Nombre"])

    print("\nEstudiantes mayores de 15 años:")
    print(df[df["Edad"] > 15])

def main(): # Función principal
    registrar_visitas()
    mostrar_datos()

if __name__ == "__main__": #método de depuración
    main()
