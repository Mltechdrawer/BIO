# Mascot - motor de búsqueda

**Mascot** es una *search engine* ampliamente utilizada para la **identificación de péptidos y proteínas** en espectrometría de masas. Mascot compara espectros MS/MS experimentales con espectros teóricos derivados de secuencias proteicas almacenadas en bases de datos. A diferencia de Andromeda (integrado en MaxQuant), Mascot puede usarse **como servicio web**, **servidor local** o a través de entornos como **Proteome Discoverer**.

---

### ¿Para qué sirve Mascot?

Mascot se utiliza para:

- Determinar **qué péptidos** han generado un espectro MS/MS.
- Inferir **proteínas** a partir de los péptidos identificados.
- Gestionar **modificaciones fijas y variables**, **tolerancias de masas**, y **especificidades enzimáticas**.
- Evaluar la **confianza de identificación** mediante probabilidad estadística (*Ion Score*, *Protein Score*) y control de FDR.

Mascot utiliza un modelo estadístico basado en **probabilidades** para determinar si una coincidencia entre espectros es significativa o pudo ocurrir por azar.

---

### ¿Cómo se usa Mascot?

1. **Acceder a Mascot**
   - Opción online pública (datos de prueba):  
     https://www.matrixscience.com/search_form_select.html
   - Instalación en servidor (licencia requerida):  
     https://www.matrixscience.com

2. **Preparar los datos**
   - Espectros MS/MS en formatos como `.mgf`, `.mzML` o exportados desde plataformas como Proteome Discoverer o MaxQuant.
   - Base de datos proteica en formato FASTA (ej. UniProt):  
     https://www.uniprot.org

3. **Configurar la búsqueda**
   - Seleccionar la **base de datos** (ej. *Uniprot_SwissProt*).
   - Elegir la **enzima** (ej. *Trypsin*).
   - Definir **tolerancias de masa**:
     - Precursor: típicamente 10–20 ppm (Orbitrap)
     - Fragmentos: 0.5–0.8 Da (ion trap)
   - Establecer **modificaciones**:
     - Fijas: Carbamidometilación (C)
     - Variables: Oxidación (M), Fosforilación (STY), etc.

4. **Ejecutar la búsqueda**
   - Mascot genera puntuaciones (*Ion Score*) que se comparan con un umbral estadístico.

5. **Interpretar resultados**
   - Reportes típicos:
     - Lista de **péptidos identificados**
     - **Proteínas inferidas**
     - FDR y significancia estadística
   - Exportable a herramientas de análisis posteriores (Perseus, Skyline, R, Python).

---

### Resumen

**Mascot identifica péptidos y proteínas comparando espectros MS/MS con bases de datos proteicas usando un modelo probabilístico.** Puede usarse en web, servidor local o integrado en software de análisis proteómico.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial Mascot | https://www.matrixscience.com |
| Manual Mascot | https://www.matrixscience.com/help |
| UniProt (bases FASTA) | https://www.uniprot.org |
| Publicación original de Mascot (Perkins et al., 1999) | https://doi.org/10.1021/ac990888i |

