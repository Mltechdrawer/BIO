# Proteómica

La **proteómica** es la rama de la biología molecular que estudia el **conjunto completo de [proteínas](01_proteinas.md "Proteínas")** expresadas por una célula, tejido u organismo en un momento y condición determinados.  
A diferencia del genoma —que es estático—, el **proteoma es dinámico** y refleja la respuesta funcional de un sistema biológico ante estímulos, cambios ambientales o estados patológicos.

La proteómica, junto con la genómica y la transcriptómica, forma parte del núcleo de las llamadas **ciencias ómicas**, que permiten una comprensión global e integradora de los procesos biológicos.  
En el contexto de la **bioinformática**, la proteómica combina técnicas experimentales (principalmente basadas en espectrometría de masas) con herramientas computacionales para el procesamiento, identificación y análisis funcional de proteínas.

---

## Tipos de proteómica

### Proteómica descriptiva
Identifica y cuantifica las proteínas presentes en una muestra biológica. Permite caracterizar el proteoma de tejidos, cultivos celulares o fluidos biológicos.

### Proteómica comparativa
Analiza las diferencias en el perfil proteico entre condiciones experimentales (por ejemplo, *tejido sano vs. tumoral*), buscando proteínas diferencialmente expresadas que puedan actuar como **biomarcadores**.

### Proteómica funcional
Explora las **interacciones proteína-proteína**, las **modificaciones postraduccionales (PTMs)** y la **dinámica de los complejos proteicos**. Estas relaciones son esenciales para comprender la red funcional celular.

### Proteómica estructural
Se centra en la **estructura tridimensional** de las proteínas mediante cristalografía, RMN o criomicroscopía electrónica.  
Complementa la información funcional al mostrar cómo la estructura condiciona la actividad.

---

## Técnicas experimentales

### Separación de proteínas

#### Electroforesis bidimensional (2D-PAGE)
Permite separar proteínas según su **punto isoeléctrico (pI)** y su **peso molecular**.  
Es una técnica clásica pero limitada en resolución para proteínas hidrofóbicas o de bajo nivel de abundancia.

#### Cromatografía líquida (HPLC / LC-MS/MS)
Utiliza columnas de alta presión para separar los péptidos antes de su análisis por **espectrometría de masas (MS)**.  
Es actualmente el enfoque estándar en la proteómica moderna.

---

### Identificación y cuantificación por espectrometría de masas (MS)

La **espectrometría de masas** permite determinar la masa y la secuencia de péptidos mediante su ionización y separación según la relación masa/carga (*m/z*).

#### Métodos de ionización
- **MALDI (Matrix-Assisted Laser Desorption/Ionization):** ideal para proteínas grandes o mezclas simples.  
- **ESI (Electrospray Ionization):** más adecuada para acoplamiento con LC y análisis de muestras complejas.

#### Tipos de analizadores
- **TOF (Time-of-Flight):** mide el tiempo que tardan los iones en recorrer un tubo de vuelo.  
- **Orbitrap:** ofrece alta resolución y precisión de masa.  
- **Q-TOF:** combina cuadrupolo y TOF para una identificación más sensible.

#### Métodos de cuantificación
- **Con marcaje isotópico:** SILAC, iTRAQ, TMT → permiten comparación directa entre muestras.  
- **Sin marcaje (label-free):** basados en la intensidad del espectro o el recuento de picos.

---

## Análisis bioinformático de datos proteómicos

El análisis computacional es esencial para convertir los espectros de masas en información biológica interpretable.

### Flujo de trabajo típico
1. **Preprocesamiento de datos:** eliminación de ruido, normalización y calibración de espectros.  
2. **Identificación de péptidos:** comparación con bases de datos de secuencias teóricas (*search engines* como [Mascot](04_mascotm.md "Mascot"), [Andromeda](04_andromeda.md "Andromeda"), [SEQUEST](04_sequest.md "SEQUEST") o [X!Tandem](04_xtandem.md "X!Tandem")).  
3. **Cuantificación:** cálculo de abundancia relativa o absoluta.  
4. **Validación:** control del error y estimación del **FDR (False Discovery Rate)**.  
5. **Análisis funcional:** clasificación GO, rutas metabólicas, y redes de interacción.

### Software y plataformas
- [**MaxQuant**](04_maxquant.md "MaxQuant")(acoplado a Andromeda)  
- [**Proteome Discoverer**](04_proteomediscoverer.md "Proteome Discover") (Thermo)  
- [**Mascot**](04_mascotp.md "Mascot") (Matrix Science)  
- [**Skyline**](04_skyline.md "Skyline") (para cuantificación dirigida)  

Estas herramientas permiten automatizar el procesamiento de espectros, la búsqueda en bases de datos y la exportación de resultados en formatos estándar (mzML, mzIdentML).

---

## Bases de datos proteómicas

| Base de datos | Contenido principal | Aplicación |
|----------------|--------------------|-------------|
| **UniProtKB / Swiss-Prot** | Secuencias de proteínas revisadas manualmente | Identificación y anotación funcional |
| **PDB (Protein Data Bank)** | Estructuras 3D de proteínas y complejos | Modelado estructural |
| **PRIDE (Proteomics Identifications Database)** | Depósito de resultados de espectrometría de masas | Reutilización de datasets experimentales |
| **PeptideAtlas / ProteomeXchange** | Repositorios de referencia global | Acceso unificado a datos proteómicos |
| **STRING / BioGRID** | Redes de interacción proteína-proteína | Análisis de conectividad funcional |
| **PhosphoSitePlus** | Modificaciones postraduccionales | Estudios de fosforilación y regulación enzimática |

---

## Análisis funcional

El siguiente paso tras la identificación es **interpretar el significado biológico** de las proteínas detectadas.

### Enriquecimiento funcional
- **Gene Ontology (GO):** clasificación de proteínas según su función molecular, componente celular y proceso biológico.  
- **Reactome y KEGG:** mapeo de proteínas en rutas metabólicas o de señalización.  
- **g:Profiler y DAVID:** herramientas de análisis automático de enriquecimiento funcional.

### Redes de interacción proteína-proteína
Las proteínas raramente actúan solas.  
El análisis de redes (por ejemplo, mediante **STRING**) permite detectar módulos funcionales, hubs de interacción y posibles dianas terapéuticas.

---

## Proteómica cuantitativa y diferencial

### Enfoques experimentales
- Comparación de muestras biológicas mediante marcaje isotópico (iTRAQ, TMT) o métodos *label-free*.  
- Detección de proteínas **diferencialmente expresadas** entre condiciones experimentales.

### Análisis estadístico
- Normalización de intensidades (log2, z-score).  
- Pruebas t, ANOVA, o modelos lineales (limma, MSstats).  
- Control del **FDR (False Discovery Rate)** mediante Benjamini-Hochberg.

El objetivo es identificar proteínas cuya abundancia varíe significativamente, lo que puede reflejar cambios funcionales o patológicos.

---

## Integración multi-ómica

La integración de la proteómica con otras capas de información permite un enfoque más completo del sistema biológico.

- **Genómica + Transcriptómica + Proteómica:** correlación entre expresión génica y abundancia proteica.  
- **Proteómica + Metabolómica:** relación entre enzimas y sus productos metabólicos.  
- **Modelos integrados (multi-omics):** reconstrucción de redes regulatorias y modelado de fenotipos celulares.

---

## Aplicaciones de la proteómica

### Medicina personalizada
Identificación de **biomarcadores diagnósticos** y pronósticos (por ejemplo, proteínas plasmáticas asociadas a cáncer o inflamación).

### Descubrimiento de fármacos
Detección de **dianas terapéuticas** y seguimiento de respuestas farmacológicas mediante análisis proteómico comparativo.

### Biotecnología y agricultura
Optimización de cultivos, fermentaciones y producción de enzimas mediante el estudio del proteoma funcional.

### Ecología y microbiología
Caracterización del **proteoma ambiental o microbiano** en estudios de microbiomas y procesos biogeoquímicos.

---

## Conclusiones

La proteómica proporciona una visión funcional del sistema biológico, completando la información aportada por el genoma y el transcriptoma.  
El uso de métodos computacionales y estadísticos es esencial para manejar la gran cantidad de datos generados por la espectrometría de masas y para obtener conclusiones biológicamente significativas.  

La **bioinformática proteómica** es, por tanto, una disciplina integradora, situada en el cruce entre la biología molecular, la estadística y la ciencia de datos. 

---

[Ejemplo Práctico](04_ejercicios_proteomica0.md "Ejemplo Práctico")

[Ejercicio Proteómica](04_ejercicios_proteomica1.md "Ejercicio Proteómica")