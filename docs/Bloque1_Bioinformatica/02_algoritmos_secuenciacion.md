# Algoritmos de Secuenciación

La secuenciación del ADN y ARN es un proceso esencial en bioinformática. Existen diversos **algoritmos** que permiten ensamblar, alinear, corregir y validar secuencias genéticas. En este documento se resumen los principales enfoques y herramientas utilizadas actualmente.

---

## Algoritmos de ensamblaje *de novo*

Los algoritmos *de novo* ensamblan secuencias sin una referencia previa, reconstruyendo genomas completos a partir de fragmentos cortos.

### Grafos de De Bruijn

Uno de los enfoques más utilizados para el ensamblaje *de novo* es el **grafo de De Bruijn**, especialmente eficaz con secuencias cortas generadas por tecnologías NGS.  
Los caminos dentro del grafo representan las posibles reconstrucciones de la secuencia original.

**Ejemplos de programas:**

- **Velvet** → pionero en el uso del grafo de De Bruijn para ensamblajes *de novo*. Muy eficiente con lecturas cortas.  
- **SPAdes (St. Petersburg genome assembler)** → ideal para genomas bacterianos y metagenómicos.  
- **ABySS** → apto tanto para genomas pequeños como grandes (por ejemplo, el genoma humano), diseñado para lecturas masivas de Illumina.

---

## Algoritmos de superposición-consenso

Estos algoritmos son adecuados para lecturas largas (como las de **PacBio** u **Oxford Nanopore**). Se basan en detectar superposiciones directas entre las lecturas.

**Ejemplos de programas:**

- **Celera Assembler** → empleado en el *Proyecto Genoma Humano*.  
- **Canu** → evolución de Celera, optimizado para lecturas largas.

---

## Algoritmos basados en referencia

Cuando se dispone de un genoma de referencia, las lecturas se alinean con él.

### Alineamiento de lecturas

**Herramientas principales:**

- **BWA (Burrows–Wheeler Aligner)** → ampliamente utilizado para lecturas cortas. Usa el índice Burrows–Wheeler para acelerar búsquedas.  
- **Bowtie2** → rápido y eficiente en memoria; útil para lecturas cortas y medianas.  
- **Minimap2** → diseñado para lecturas largas; rápido en el alineamiento de genomas completos.

### Detección de variantes y reensamblaje

Algunos algoritmos no solo alinean, sino que también identifican **variantes genéticas** (mutaciones) o corrigen errores locales.

**Herramientas destacadas:**

- **GATK (Genome Analysis Toolkit)** → kit de herramientas muy popular para detectar variantes, recalibrar calidad y analizar alineamientos.  
- **FreeBayes** → identifica variantes genéticas (SNPs e *indels*) mediante modelos probabilísticos.

---

## Algoritmos híbridos

Los métodos híbridos combinan enfoques de grafos de De Bruijn (para fragmentos cortos) y superposición-consenso (para lecturas largas), aprovechando las ventajas de ambos.

**Ejemplos de ensambladores híbridos:**

- **MaSuRCA** → combina secuencias cortas y largas para un ensamblaje más preciso.  
- **HGAP (Hierarchical Genome Assembly Process)** → desarrollado por PacBio, usa múltiples estrategias para lecturas largas.

---

## Algoritmos de corrección de errores

Las lecturas pueden contener errores, por lo que algunos programas los corrigen antes del ensamblaje o alineamiento.

**Herramientas destacadas:**

- **Pilon** → mejora la calidad de ensamblajes corrigiendo bases, cerrando huecos y refinando la secuencia.  
- **Quiver** → diseñado para secuencias PacBio; utiliza la información de calidad para corregir errores.

---

## Algoritmos de evaluación y validación

Tras el ensamblaje o alineamiento, es necesario evaluar la calidad del resultado.

**Principales herramientas:**

- **QUAST (Quality Assessment Tool for Genome Assemblies)** → compara el ensamblaje con referencias conocidas o mide métricas independientes como el tamaño del ensamblaje y número de *contigs*.  
- **BUSCO (Benchmarking Universal Single-Copy Orthologs)** → evalúa la integridad del ensamblaje mediante genes ortólogos conservados.

---

