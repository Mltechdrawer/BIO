# Sequest

**SEQUEST** es una de las *search engines* pioneras en la **identificación de péptidos** a partir de espectrometría de masas en proteómica. Desarrollado inicialmente por John Yates y colaboradores, SEQUEST compara los espectros MS/MS experimentales con espectros teóricos generados mediante **fragmentación in silico** de las secuencias en una base de datos FASTA.  

SEQUEST es uno de los motores de búsqueda centrales dentro de software como **Proteome Discoverer (Thermo Scientific)**, aunque también existen variantes como **Comet** (versión libre y abierta basada en SEQUEST).

---

### ¿Para qué sirve SEQUEST?

SEQUEST se utiliza para:

- Identificar **péptidos** comparando espectros MS/MS con espectros teóricos.
- **Inferir proteínas** utilizando las relaciones péptido-proteína.
- Definir parámetros como **enzima**, **modificaciones**, **tolerancia de masas**.
- Evaluar la **confianza** mediante puntuaciones específicas (*XCorr*, *ΔCn*) y filtrado FDR.

SEQUEST emplea el algoritmo de correlación cruzada **XCorr**, que mide cuán bien se superponen los picos del espectro experimental con los del espectro teórico.

---

### ¿Cómo se usa SEQUEST?

1. **Software habitual**
   - **Proteome Discoverer (Thermo Scientific)** — entorno GUI oficial.
   - **Comet** — implementación libre inspirada en SEQUEST:  
     https://comet-ms.sourceforge.io

2. **Preparar los datos**
   - Espectros MS/MS en formatos como `.raw`, `.mzML` o `.mgf`.
   - Base de datos proteica en formato FASTA:  
     https://www.uniprot.org

3. **Configurar la búsqueda en Proteome Discoverer**
   - Añadir los archivos de espectrometría.
   - Seleccionar el **nodo** SEQUEST (o Comet).
   - Definir parámetros típicos:
     - **Enzima:** *Trypsin/P*
     - **Tolerancia de precursor:** 10–20 ppm (Orbitrap habitual)
     - **Tolerancia de fragmentos:** 0.6–0.8 Da (CID) o más estricta en HCD de alta resolución
     - **Modificaciones fijas:** Carbamidometilación (C)
     - **Modificaciones variables:** Oxidación (M), Acetilación (N-terminal), Fosforilación (S/T/Y) si se requiere

4. **Ejecutar**
   - El motor SEQUEST generará valores **XCorr** y **ΔCn** para evaluar la calidad de la coincidencia.

5. **Interpretar los resultados**
   - Se combinan con un **validador** (ej.: Percolator) para aplicar **FDR ≤ 1%**.
   - Resultados finales:
     - Lista de péptidos identificados
     - Proteínas inferidas
     - Métricas de confianza por identificación

---

### Resumen

**SEQUEST identifica péptidos midiendo la correlación entre espectros MS/MS experimentales y espectros teóricos.**  
Se usa principalmente a través de **Proteome Discoverer**, y su métrica central es **XCorr**, complementada con control de FDR.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Thermo Proteome Discoverer | https://www.thermofisher.com/proteomediscoverer |
| Comet (SEQUEST-like open source) | https://comet-ms.sourceforge.io |
| UniProt (FASTA) | https://www.uniprot.org |
| Publicación original de SEQUEST (Eng, McCormack & Yates, 1994) | https://doi.org/10.1002/mas.1280260109 |

