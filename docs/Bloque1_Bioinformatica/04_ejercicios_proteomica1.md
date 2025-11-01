# Ejercicio

La espectrometría de masas genera grandes volúmenes de datos que deben ser procesados y analizados computacionalmente.  
En esta práctica utilizaremos **datos reales de proteómica depositados en PRIDE**, el principal repositorio público de resultados proteómicos, y aprenderemos a interpretarlos mediante herramientas bioinformáticas.

---

### Objetivo

Explorar un conjunto de datos de proteómica cuantitativa para:

- Comprender el flujo de trabajo de análisis desde el experimento hasta la interpretación biológica.    
- Identificar proteínas detectadas, cuantificarlas y realizar un análisis funcional básico.    
- Aplicar herramientas como **MaxQuant** y **Perseus** en el análisis de datos reales.  

---

### Paso 1. Acceso al repositorio PRIDE

1. Entra en el portal:  
   👉 [https://www.ebi.ac.uk/pride/](https://www.ebi.ac.uk/pride/)
2. En el buscador principal, escribe:  
Proteomic profiling of human plasma
(u otro término como *label-free quantitative proteomics*, *iTRAQ* o *cancer proteome*).  
3. Selecciona uno de los estudios sugeridos (por ejemplo, **PXD025292**: *Quantitative proteomics of human plasma*).  
4. Abre la pestaña **Files** y descarga los ficheros de resultados:  
- `proteinGroups.txt` o `.csv` (identificación y cuantificación).  
- `metadata.txt` o `.sdrf.tsv` (información del experimento).  

---

### Paso 2. Exploración inicial con MaxQuant

1. Abre el programa **MaxQuant** ([descarga gratuita](https://www.maxquant.org)).  
2. Carga los archivos descargados (`raw` o `txt`).  
3. Verifica las opciones de búsqueda:
- Base de datos de referencia: **UniProt Homo sapiens (Swiss-Prot)**.  
- Search engine: **Andromeda** (por defecto).  
4. Ejecuta el análisis (*Run*) para generar la tabla de proteínas identificadas.  

El resultado incluirá:

- Lista de proteínas con su identificación (ID UniProt).    
- Intensidades normalizadas (*LFQ intensity*).    
- Número de péptidos únicos detectados por proteína.  

---

### Paso 3. Análisis diferencial en Perseus

1. Abre **Perseus** ([descarga gratuita](https://maxquant.net/perseus/)).  
2. Importa el archivo `proteinGroups.txt` generado por MaxQuant.  
3. Filtra las proteínas con datos ausentes o baja calidad.  
4. Añade las etiquetas de condición experimental (*Group A / Group B*, *control / treated*).  
5. Aplica:
- Normalización log₂.  
- Prueba t o ANOVA para detectar **proteínas diferencialmente expresadas**.  
- Corrección FDR (Benjamini–Hochberg).  
6. Genera:
- Gráfico de dispersión (volcano plot).  
- Heatmap de proteínas significativas.

---

### Paso 4. Análisis funcional

1. Copia las **IDs de UniProt** de las proteínas significativas.  
2. Abre la herramienta [g:Profiler](https://biit.cs.ut.ee/gprofiler/gost) o [DAVID](https://david.ncifcrf.gov/).  
3. Realiza un **análisis de enriquecimiento funcional** para identificar:
- Procesos biológicos predominantes (*Gene Ontology*).  
- Rutas metabólicas (*KEGG / Reactome*).  
- Componentes celulares (*Cytosol, Mitochondrion, Membrane…*).  

---

### Paso 5. Visualización en STRING

1. Accede a [https://string-db.org](https://string-db.org).  
2. Pega las proteínas más relevantes (ID de UniProt).  
3. Genera una **red de interacciones proteína-proteína (PPI)**.  
- Ajusta el *confidence score* a ≥0.7 (alta confianza).  
4. Interpreta los módulos funcionales y posibles complejos proteicos.  

---

### Paso 6. Cuestiones para reflexionar

1. ¿Qué proteínas mostraron mayor variación entre condiciones experimentales?  
2. ¿Qué funciones biológicas o rutas están más representadas?  
3. ¿Qué tipo de patrones se observan en la red PPI?  
4. ¿Cómo se podrían integrar estos resultados con transcriptómica o metabolómica?  

---

### Paso 7. (Opcional) Integración multi-ómica  

Si dispones de datos de expresión génica o transcriptómica del mismo experimento (por ejemplo, en GEO o ArrayExpress):

1. Relaciona los niveles de proteína y ARN para los genes coincidentes.  
2. Analiza la correlación entre ambas capas.  
3. Reflexiona sobre posibles mecanismos post-transcripcionales.

---

### Conclusión

Esta práctica permite al alumnado:

- Familiarizarse con el **flujo de trabajo bioinformático en proteómica**.    
- Comprender cómo los espectros se convierten en datos biológicos interpretables.    
- Explorar la **variabilidad y complejidad del proteoma** en un contexto experimental real.  

La proteómica moderna combina instrumentación de alta resolución con algoritmos avanzados, abriendo nuevas oportunidades para la **medicina de precisión** y el **descubrimiento de biomarcadores**.

