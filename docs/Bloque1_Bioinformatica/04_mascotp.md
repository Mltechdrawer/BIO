# Mascot - plataforma

**Mascot** es una plataforma de análisis de espectrometría de masas desarrollada por **Matrix Science**, que incluye un **buscador (search engine) de péptidos y proteínas** accesible a través de **web** o **servidor local**. Mascot compara espectros MS/MS experimentales con espectros teóricos derivados de secuencias en bases de datos FASTA, y asigna una puntuación estadística que indica la probabilidad de que la coincidencia sea real.

Puede funcionar como:
- Servicio **online** (para datos pequeños o demostraciones)
- **Servidor local** en un laboratorio (opción habitual)
- Engine integrado dentro de plataformas como **Proteome Discoverer**

---

### ¿Para qué se usa Mascot?

Mascot permite:

- Identificar **péptidos** y **proteínas** a partir de datos MS/MS.
- Aplicar **modificaciones fijas y variables**.
- Definir **enzimas de digestión** y niveles de tolerancia de masa.
- Evaluar la **confianza** de la identificación mediante:
  - **Ion Score**
  - **Protein Score**
  - **E-value**
  - Control de **FDR**

Mascot utiliza una estrategia estadística basada en **probabilidad de coincidencia al azar**.

---

### ¿Cómo se usa Mascot?

1. **Acceso**
   - Plataforma online para pruebas:  
     https://www.matrixscience.com/search_form_select.html
   - Instalación local (requiere licencia):
     https://www.matrixscience.com

2. **Preparar los datos**
   - Archivos de espectros: `.mgf`, `.mzML` o exportados desde Proteome Discoverer / MaxQuant.
   - Base de datos FASTA (ej. **UniProt**):  
     https://www.uniprot.org

3. **Configurar la búsqueda**
   - Seleccionar **base de datos** (ej. UniProt_SwissProt).
   - Definir **enzima** (ej. *Trypsin/P*).
   - Establecer **tolerancias**:
     - Precursor: 10–20 ppm (Orbitrap estándar)
     - Fragmento: 0.5–0.8 Da (CID) o menor si HCD alta resolución.
   - Modificaciones:
     - **Fijas:** Carbamidometilación (C)
     - **Variables:** Oxidación (M), Fosforilación (S/T/Y), Acetilación (N-ter)

4. **Ejecutar búsqueda**
   - Mascot generará una lista de coincidencias ordenada por **Ion Score**.

5. **Interpretar resultados**
   - Identificaciones a nivel de péptido y proteína.
   - Verificación mediante **E-value** y **umbral de significancia**.
   - Filtrado adicional por **FDR** (a veces realizado en software externo como **Percolator** o **Proteome Discoverer**).

---

### Resumen

**Mascot es una plataforma web/servidor para identificación de péptidos y proteínas**, basada en modelos probabilísticos y ampliamente utilizada en flujos proteómicos académicos e industriales. Puede funcionar sola o integrada en Proteome Discoverer.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial Mascot | https://www.matrixscience.com |
| Servidor de prueba Mascot | https://www.matrixscience.com/search_form_select.html |
| Manual de Mascot | https://www.matrixscience.com/help |
| Publicación original (Perkins et al., 1999, *Analytical Chemistry*) | https://doi.org/10.1021/ac990888i |
| UniProt (bases FASTA) | https://www.uniprot.org |
