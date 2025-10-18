# Ejemplo de matriz de expresión génica

Imagina que se han analizado **cinco genes** en **tres muestras** (por ejemplo, tres condiciones biológicas o tres pacientes).  
Cada valor representa el nivel de expresión medido —podría ser en **recuentos**, **FPKM** o **TPM**, según el método de normalización.

---

## Ejemplo de matriz de expresión (valores TPM)

| **Gen**     | **Muestra_1** | **Muestra_2** | **Muestra_3** |
|--------------|---------------|---------------|---------------|
| **GeneA**    | 12.4          | 15.2          | 9.8           |
| **GeneB**    | 0.5           | 0.8           | 0.3           |
| **GeneC**    | 48.9          | 51.3          | 62.7          |
| **GeneD**    | 103.2         | 98.6          | 110.1         |
| **GeneE**    | 7.1           | 6.9           | 8.2           |

---

## Interpretación

- Cada **fila** representa un gen (GeneA–GeneE).  
- Cada **columna** representa una muestra.  
- Los números son los **niveles de expresión** estimados.  
- Si, por ejemplo, **GeneD** tiene valores mucho más altos, significa que está **altamente expresado** en todas las muestras.  
- Si **GeneC** aumenta en la Muestra_3, podría indicar una **respuesta diferencial** en esa condición.

---

## Aplicaciones

Esta matriz es el **punto de partida** para análisis más avanzados, como:
- Comparar expresión entre condiciones (expresión diferencial).  
- Analizar correlaciones entre genes (coexpresión).  
- Clasificar muestras o detectar patrones con PCA o clustering jerárquico.
