# Actividad práctica:
## Visualización de marcas epigenéticas en UCSC Genome Browser

Esta práctica tiene como objetivo explorar visualmente las **marcas epigenéticas de histonas** utilizando datos reales del proyecto **ENCODE** a través del **UCSC Genome Browser**.  
Aprenderás a identificar regiones activas o reprimidas en el genoma humano y a interpretar cómo las modificaciones de histonas se relacionan con la regulación de la expresión génica.

---

### Paso 1. Acceso al navegador genómico

1. Abre el sitio web del UCSC Genome Browser:  
   [https://genome.ucsc.edu](https://genome.ucsc.edu)
2. En el panel principal, selecciona:
   - **Genome:** Human  
   - **Assembly:** GRCh38/hg38  
3. En el cuadro de búsqueda escribe: SHH 
(correspondiente al gen *Sonic Hedgehog*).  
Pulsa **Go**.

---

### Paso 2. Activar el hub de datos ENCODE

1. En la barra superior del UCSC, ve a **My Data → Track Hubs**.  
2. En la pestaña **Public Hubs**, localiza el siguiente hub y pulsa **Connect**: ENCODE DNA Trackhub 
3. Asegúrate de usar el ensamblado **hg38**.

Esto cargará las pistas con datos experimentales de ENCODE (ChIP-seq, DNase-seq, etc.).

---

### Paso 3. Buscar y activar la marca H3K27ac

1. En el panel superior del navegador, haz clic en **Track search** (parte inferior de la vista genómica).  
2. En el campo de búsqueda escribe:  H3K27ac
y pulsa **Search**.  
3. Entre los resultados, selecciona la pista llamada: Layered H3K27ac Mark (Often Found Near Regulatory Elements)
4. Haz clic en **View in Genome Browser**.

---

### Paso 4. Interpretar la vista

Verás una imagen similar a la siguiente:
| Layered H3K27ac Mark (ENCODE) |

Los **picos de color** representan regiones del ADN donde se ha detectado **acetilación en la lisina 27 de la histona H3 (H3K27ac)**.  
Esta modificación epigenética indica la presencia de **promotores y enhancers activos**.

- Regiones con **alta señal (picos altos o color intenso)** → enhancers activos.  
- Regiones con **poca o nula señal** → ADN inactivo o compactado.  

Además, justo encima verás la pista: ENCODE Candidate Cis-Regulatory Elements (cCREs)

que muestra las regiones reguladoras identificadas por ENCODE.  
La coincidencia de ambas pistas (H3K27ac + cCREs) indica **actividad transcripcional activa**.

---

### Paso 5. Explora otras marcas

Repite la búsqueda del **Paso 3** con las siguientes marcas para comparar:

| Marca | Tipo de modificación | Interpretación |
|-------|----------------------|----------------|
| **H3K4me3** | Trimetilación de la lisina 4 de H3 | Promotores activos (pico estrecho en el TSS) |
| **H3K27me3** | Trimetilación de la lisina 27 de H3 | Regiones reprimidas (marca de Polycomb) |

Cada una puede activarse y visualizarse al mismo tiempo para observar la relación entre **activación** (H3K4me3, H3K27ac) y **represión** (H3K27me3) en un mismo gen.

---

### Paso 6. Análisis y reflexión

Responde en tu cuaderno o en el campus virtual:

1. ¿Qué tipo de regiones (promotores, enhancers, cuerpos de gen) muestran mayor señal de H3K27ac en el gen *SHH*?
2. ¿Coinciden las zonas de alta señal de H3K27ac con las regiones cCREs? ¿Qué indica esto?
3. ¿Qué diferencia observas entre los patrones de H3K4me3 y H3K27me3?  
4. ¿Cómo se relacionan estas observaciones con el nivel esperado de expresión del gen?

---

### Conclusión

Esta práctica permite comprender cómo las **marcas de histonas reflejan el estado funcional del genoma**, y cómo la **epigenética regula la expresión génica sin modificar la secuencia del ADN**.  
El UCSC Genome Browser es una herramienta poderosa para **visualizar datos reales** de proyectos internacionales como **ENCODE** o **Roadmap Epigenomics**.

