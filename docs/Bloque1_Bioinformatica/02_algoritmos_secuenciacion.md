# Algoritmos de ensamblaje de secuencias

## Introducción
La secuenciación moderna no produce genomas completos de una sola lectura, sino millones de fragmentos que deben ser **reconstruidos** computacionalmente. Esta tarea, conocida como **ensamblaje de secuencias**, es uno de los grandes retos de la bioinformática: exige algoritmos eficientes, capaces de lidiar con errores, regiones repetitivas y grandes volúmenes de datos.

---

## Algoritmos clásicos (visión histórica)

### Algoritmos *greedy* (avaro)
Los primeros intentos de ensamblaje se basaron en estrategias *greedy*, que unen secuencias siempre que se detecta un solapamiento suficientemente largo. Aunque sencillos, estos algoritmos eran muy sensibles a errores y repeticiones, lo que limitaba su utilidad en genomas reales.

[Greedy Assembly](greedy_assembly.py)

[Greedy diagrama](olc_walkthrough.md)


### Overlap–Layout–Consensus (OLC)
El paradigma OLC fue dominante durante la era de la secuenciación de Sanger. Consta de tres pasos: (1) encontrar solapamientos entre lecturas, (2) construir un grafo de disposición (*layout*), y (3) generar una secuencia consenso. Funcionó bien para proyectos como el **Proyecto Genoma Humano**, pero resultó ineficiente con la explosión de datos de la secuenciación masiva.

[Overlap Layout Consensus Assembly](olc_assembly.py)

[Overlap Layout Consensus diagrama](olc_walkthrough.md)

---

## Grafos de de Bruijn: el estándar para lecturas cortas

Con la llegada de la **secuenciación de nueva generación (NGS)**, que produce millones de lecturas cortas (50–300 pb), los algoritmos OLC dejaron de ser viables. El gran salto lo dieron los **grafos de de Bruijn**:

- Se fragmentan las lecturas en subcadenas de longitud *k* (*k-mers*).
- Cada *k-mer* es un nodo en el grafo.
- Los arcos representan solapamientos de *k-1* bases.
- El problema del ensamblaje se convierte en recorrer un camino euleriano que cubra todos los arcos.

Este enfoque es mucho más eficiente en memoria y tiempo que OLC para grandes volúmenes de lecturas cortas.

### Problemas y soluciones
- **Errores de secuenciación** generan nodos espurios. → Se corrigen mediante algoritmos de limpieza (*error correction*).
- **Repeticiones** crean bifurcaciones ambiguas. → Estrategias de simplificación del grafo (*tip removal*, *bubble popping*).
- **Selección del tamaño de *k***: compromete resolución y conectividad.

[DeBrujin Assembly](debruijn_assembly.py)

[Debrujin diagrama](debruijn_walkthrough.md)

---

## Variantes y mejoras de los grafos de de Bruijn

- **Multik-mers**: uso de varios valores de *k* en paralelo (ej. SPAdes).
- **Grafos dispersos (sparse de Bruijn)**: reducen drásticamente la memoria necesaria.
- **Omnitigs** y extensiones teóricas: garantizan secuencias correctas bajo ciertas condiciones.
- **Ensambladores híbridos**: combinan estrategias de de Bruijn con enfoques OLC o lecturas largas.

---

## Ensamblaje con lecturas largas

Las tecnologías **PacBio** y **Oxford Nanopore** generan lecturas largas (10–100 kb), muy útiles para resolver repeticiones, pero con tasas de error elevadas. Aquí resurgen los métodos tipo OLC y *string graphs*, adaptados a este contexto:

- **Canu** y **Flye**: ensambladores especializados en lecturas largas.
- **ABruijn**: adapta grafos de de Bruijn a lecturas largas con corrección de errores.
- **Etapas de pulido (*polishing*)**: herramientas como **Pilon** o **Racon** corrigen errores posteriores al ensamblaje.

---

## Ejemplos de ensambladores populares
- **Velvet**: pionero en aplicar grafos de de Bruijn a lecturas cortas.
- **SPAdes**: ampliamente utilizado, combina *multik-mers* y correcciones.
- **SOAPdenovo**: orientado a genomas grandes.
- **Canu**: referencia para lecturas largas.
- **Flye**: eficiente para genomas microbianos y metagenomas con lecturas largas.

---

## Consideraciones prácticas y desafíos actuales
- Escalabilidad en genomas grandes y complejos.
- Manejo de regiones repetitivas largas (centrómeros, telómeros).
- Ensamblajes híbridos (lecturas cortas + largas).
- Desarrollo de grafos de **pangenoma**, que representan la variabilidad genética de poblaciones completas.

---

## Resumen
1. **Greedy y OLC** → métodos históricos, útiles para comprender los orígenes.
2. **Grafos de de Bruijn** → estándar para lecturas cortas (Illumina).
3. **Variantes de de Bruijn** → multik, dispersos, híbridos.
4. **Lecturas largas (PacBio, Nanopore)** → resurgen enfoques OLC adaptados.
5. **Ensambladores actuales** → SPAdes, Velvet, Canu, Flye, entre otros.

Los algoritmos de ensamblaje son un área dinámica de la bioinformática, en constante evolución conforme aparecen nuevas tecnologías de secuenciación y aumentan las demandas de precisión y escala.
