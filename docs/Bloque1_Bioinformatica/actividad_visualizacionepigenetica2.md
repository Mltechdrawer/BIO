# Actividad práctica: 
## Exploración de la metilación del ADN en datos públicos

La **metilación del ADN** es una de las principales marcas epigenéticas implicadas en la regulación de la expresión génica.  
En esta práctica, exploraremos cómo la metilación se distribuye en el genoma humano y cómo se relaciona con la actividad de los genes, utilizando recursos del **ENCODE Project** y **GEO DataSets (NCBI)**.

---

### Paso 1. Conceptos previos

Recuerda:
- La **metilación** se produce principalmente en **dinucleótidos CpG**.  
- La **hipermetilación** de promotores suele asociarse con **represión transcripcional**.  
- La **hipometilación** en enhancers o regiones activas se asocia con **mayor expresión**.

---

### Paso 2. Visualizar datos de metilación en UCSC Genome Browser

1. Abre el **UCSC Genome Browser**:  
   [https://genome.ucsc.edu](https://genome.ucsc.edu)
2. Selecciona:
   - **Genome:** Human  
   - **Assembly:** GRCh38/hg38  
3. En el campo de búsqueda, introduce: BRCA1
(*gen conocido por su regulación epigenética en cáncer de mama*).
4. Pulsa **Go**.

---

### Paso 3. Activar pistas de metilación (bisulfito-seq)

1. En la vista del genoma, ve al menú inferior y selecciona **Track search**.  
2. En el cuadro de búsqueda escribe: DNA methylation ENCODE
y pulsa **Search**.
3. Busca una pista con un nombre similar a:  
ENCODE DNA Methylation Track (WGBS)
(*Whole-Genome Bisulfite Sequencing*).  
4. Haz clic en **View in Genome Browser** y selecciona **pack** o **full** para visualizarla.

---

### Paso 4. Interpretar la vista

La pista mostrará un perfil de metilación en escala de color o altura:  
- **Altos niveles (color oscuro o picos altos)** → alta metilación (CpG metilado).  
- **Bajos niveles (color claro o picos bajos)** → hipometilación (CpG desmetilado).

Observa:
- ¿Qué patrón de metilación presenta el **promotor de BRCA1**?  
- ¿Hay diferencias entre las regiones génicas y las intergénicas?  
- ¿Coinciden las zonas hipometiladas con regiones activas (como las vistas en H3K27ac en la actividad anterior)?

---

### Paso 5. Comparar distintos tejidos (opcional)

1. En la misma pista o desde el menú de configuración, selecciona diferentes líneas celulares (por ejemplo, **MCF-7**, **H1-hESC**, **K562**).  
2. Observa cómo cambia la metilación de **BRCA1** entre tejidos sanos y líneas tumorales.

---

### Paso 6. Búsqueda de datos experimentales en GEO

1. Abre el portal de **GEO Datasets**:  
[https://www.ncbi.nlm.nih.gov/gds](https://www.ncbi.nlm.nih.gov/gds)
2. En el cuadro de búsqueda escribe: BRCA1 methylation human 
3. Examina algunos estudios (por ejemplo, análisis de metilación en cáncer).  
Fíjate en las columnas:
- **Organism**  
- **Platform** (por ejemplo, *Illumina HumanMethylation450 BeadChip*).  
- **Summary** (te explicará qué regiones se metilaron diferencialmente).  
4. Si el estudio incluye un enlace “**View on UCSC Genome Browser**”, ábrelo para explorar los datos directamente.

---

### Paso 7. Preguntas para reflexionar

1. ¿Qué relación observas entre el nivel de metilación del promotor y la posible expresión de **BRCA1**?  
2. ¿Qué diferencias aparecen entre tejidos o líneas celulares?  
3. ¿Qué ventajas tiene usar datos de **bisulfito-seq** frente a arrays de metilación (450k/850k)?  
4. ¿Podrías combinar esta información con las marcas de histonas (H3K27ac, H3K4me3) para inferir el estado epigenético completo del gen?

---

### Conclusión

Esta práctica te permitirá:
- Comprender cómo la **metilación del ADN regula la expresión génica**.  
- Visualizar **datos reales de bisulfito-seq** de ENCODE y GEO.  
- Integrar la metilación con otras capas epigenéticas (como las marcas de histonas).  

---