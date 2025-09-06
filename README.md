# TRABAJO INTEGRADOR N°2 - Torres, Becerra

Este programa en **Python** permite **registrar y analizar visitas de estudiantes a un MakerSpace**.
El objetivo es organizar la información de los alumnos que ingresan, guardarla en un archivo y luego mostrar estadísticas básicas.

---

## ¿Qué resuelve?

* Facilita el **registro ordenado** de estudiantes (nombre, edad, curso y motivo de la visita).
* **Almacena los datos en un archivo CSV** para poder consultarlos más tarde.
* Permite **analizar la información** de manera rápida con Pandas:

  * Mostrar la lista completa de estudiantes registrados.
  * Contar cuántas visitas realizó cada curso.
  * Identificar al primer estudiante que ingresó.
  * Filtrar estudiantes mayores de 15 años.

---

## Funcionamiento

El programa está compuesto por **tres funciones principales**:

1. **`registrar_visitas()`**

   * Pide datos de los estudiantes al usuario (Nombre, Edad, Curso, Motivo).
   * Almacena la información en un **diccionario de listas**.
   * Convierte los datos en un **DataFrame de Pandas**.
   * Guarda los datos en un archivo **CSV** (`visitas_makerspace.csv`).

2. **`mostrar_datos()`**

   * Lee el archivo CSV con `pd.read_csv()`.
   * Muestra la lista completa de registros.
   * Calcula la cantidad de visitas por curso con `Series.value_counts()`.
   * Identifica al primer estudiante registrado.
   * Filtra estudiantes mayores de 15 años.

3. **`main()`**

   * Función principal que **integra todo el proceso**.
   * Ejecuta el registro de visitas y luego muestra los datos.

El bloque:

```python
if __name__ == "__main__":
    main()
```

asegura que el programa se ejecute correctamente solo cuando se lo ejecuta directamente.

---

## Requisitos que cumple
 -    **Uso de listas y diccionarios** → para la carga inicial de datos de estudiantes.
-  **Manejo de archivos con Pandas** → uso de `to_csv` y `read_csv` para guardar y leer los datos.
- **Uso de Series y DataFrames** → manipulación de datos con Pandas (filtrado, conteo, selección).
-   **Funciones para modularizar el programa** → `registrar_visitas()`, `mostrar_datos()` y `main()`.
-  **Código ordenado y comentado** → con estructura clara y buenas prácticas de programación.
