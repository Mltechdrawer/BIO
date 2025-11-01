# Ejemplo práctico: 

## Análisis de datos proteómicos públicos

**Objetivo:** analizar un dataset de espectrometría de masas del repositorio **PRIDE** para identificar proteínas y su función biológica.

1. Accede al portal: [https://www.ebi.ac.uk/pride/](https://www.ebi.ac.uk/pride/)  
2. Busca un estudio, por ejemplo:  
Proteomic profiling of human plasma
3. Descarga uno de los archivos de resultados (por ejemplo: peptides.txt). [Representación de columnas](peptidos.md#infocolumnas).  
4. Limpia el fichero dejando solo las [columnas escenciales](peptidos.md#columnas_escenciales)
5. Resuelve los siguientes ejercicios:


# Ejercicios – Interpretación de Datos Proteómicos

**Contexto:**  
Los datos provienen de un experimento de espectrometría de masas analizado con MaxQuant.  
Cada fila representa un **péptido identificado**, y las columnas indican su **secuencia**, **a qué proteínas pertenece**, el **nivel de confianza** en la identificación y la **abundancia** del péptido en distintas muestras.

Trabajarás con el archivo que contiene solo las columnas esenciales. 

---

## Ejercicio 1 — Identificando péptidos

**Tarea:**  
Elige **un péptido** de la tabla y responde:

1. ¿Cuál es su secuencia (`Sequence`)?
2. ¿A qué proteína(s) se asocia (`Proteins`)?
3. ¿Cuál es el nombre del gen asociado (`Gene names`)?

**Objetivo:**  
Comprender que en proteómica **no se identifican proteínas directamente**:  
primero se identifican **péptidos**, que luego se asignan a proteínas.

> *Ejemplo de interpretación:*  
> “Este péptido aparece en dos proteínas diferentes, lo que sugiere que estas comparten una región común.”

---

## Ejercicio 2 — Evaluando la confianza en la identificación

**Tarea:**  
Observa el valor **`PEP`** del péptido seleccionado.

- `PEP < 0.01` → identificación **confiable**
- `PEP > 0.05` → identificación **poco confiable**

**Objetivo:**  
Entender que los datos proteómicos se basan en **probabilidad y estadística**, no en certeza absoluta.

> PEP = Probabilidad estimada de que la identificación sea incorrecta  
> Cuanto menor, mejor.

---

## Ejercicio 3 — Explorando la cuantificación entre muestras

**Tarea:**  
Compara las intensidades del mismo péptido entre dos muestras (por ejemplo, `A1` y `A10`).

- ¿Dónde es más abundante?
- ¿Está ausente (0 o vacío) en alguna muestra?

**Objetivo:**  
Interpretar la cuantificación como **datos experimentales**, que pueden variar entre muestras.

> *Ejemplo:*  
> “El péptido está más presente en A1 que en A10, lo cual podría reflejar una diferencia biológica o técnica.”

---

## Ejercicio 4 — Identificando valores faltantes

**Tarea:**  
Busca uno o dos péptidos que tengan valores faltantes (0 o vacío) en algunas muestras.

- ¿Qué podría explicar la ausencia?
  - ¿No expresión real?
  - ¿O límite de detección del instrumento?

**Objetivo:**  
Estudiar el concepto de **valores faltantes no aleatorios** (MNAR) en proteómica.

> *Idea clave:*  
> La ausencia de señal **no implica** ausencia de la proteína.

---

## Ejercicio 5 — Comparación basada en proteínas

**Tarea:**  
1. Elige una proteína o gen (por ejemplo, usando `Gene names`).  
2. Localiza todos los péptidos asociados a esa proteína.  
3. Compara sus intensidades entre dos grupos de muestras (ej. A vs B).

**Objetivo:**  
Comprender que **la proteína se cuantifica a partir de múltiples péptidos**, no de uno solo.

> *Ejemplo:*  
> “Si la mayoría de los péptidos muestran mayor intensidad en A que en B, la proteína probablemente está más abundante en A.”

---

## Ejercicio 6 — Pregunta de razonamiento

**Tarea:**  
Explica por qué es importante identificar **más de un péptido por proteína**.

---

## Ejercicio 7 — Comparación estadística entre dos grupos en R

**Tarea:**  
Evaluar si la **abundancia media** de los péptidos **difiere significativamente entre dos grupos de muestras** (por ejemplo, grupo A1–A5 vs grupo A6–A10).
---

