# Proteome Discoverer

**Proteome Discoverer (PD)** es una plataforma de análisis de **proteómica basada en espectrometría de masas** desarrollada por **Thermo Scientific**. Está diseñada como un entorno modular donde el usuario construye *pipelines* analíticos mediante **nodos**, permitiendo integrar diferentes motores de búsqueda (como **SEQUEST**, **Mascot**, **MSAmanda**, **Comet**), herramientas de cuantificación y módulos de validación estadística (como **Percolator**).

PD se utiliza ampliamente en laboratorios de proteómica que trabajan con instrumentos Orbitrap, aunque también admite datos convertidos desde otros equipos.

---

### ¿Para qué se usa Proteome Discoverer?

Se utiliza para:

- **Identificar péptidos y proteínas** a partir de datos MS/MS.
- Integrar múltiples **search engines** en un mismo análisis.
- Aplicar **correcciones, filtrados y control de FDR** de forma flexible.
- Realizar **cuantificación**, incluyendo:
  - **TMT / iTRAQ (cuantificación isobárica)**
  - **SILAC**
  - **LFQ (Label-Free Quantification)**
- Explorar **modificaciones postraduccionales** (PTMs) mediante flujos dirigidos.

---

### ¿Cómo se usa Proteome Discoverer?

1. **Importar datos**
   - Cargar archivos `.raw` u otros formatos convertidos como `.mzML`.

2. **Configurar el flujo de trabajo (Workflow)**
   - Seleccionar **nodos** según el objetivo:
     - *Spectrum Selector* → limpieza de señales
     - *Search Engine* (SEQUEST, Mascot, Comet, MSAmanda…)
     - *Percolator* → validación con FDR
     - *Protein FDR Validator* → control de nivel de proteína
     - *Quan Nodes* → análisis de cuantificación (si aplica)

3. **Parámetros típicos de búsqueda**
   - **Enzima:** Trypsin/P
   - **Tolerancia de masa del precursor:** ~10–20 ppm
   - **Tolerancia de fragmentos:** ~0.5–0.8 Da (CID) o ≤0.05 Da (HCD alta res.)
   - **Modificaciones fijas:** Carbamidometilación (C)
   - **Modificaciones variables:** Oxidación (M), Fosforilación (S/T/Y), Acetilación (N-ter)

4. **Ejecutar**
   - PD envía los espectros al motor de búsqueda seleccionado y procesa los resultados.

5. **Revisar resultados**
   - Tablas visuales interactivas:
     - **Péptidos identificados**
     - **Proteínas inferidas**
     - Valores de probabilidad / FDR
     - Si hay cuantificación → intensidades / ratios

6. **Exportar**
   - Hacia Excel, `.txt`, `.mzIdentML`, o análisis posterior en **Perseus / Skyline / R**.

---

### Resumen

**Proteome Discoverer es una plataforma modular y flexible para análisis proteómicos**, que permite integrar múltiples motores de búsqueda y flujos avanzados de identificación, cuantificación y validación estadística.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial Proteome Discoverer | https://www.thermofisher.com/proteomediscoverer |
| Documentación y manuales | https://knowledge.thermofisher.com/PD |
| Tutoriales y workflows oficiales | https://www.thermofisher.com/learningcenter |
| Publicación original de SEQUEST (algoritmo central en PD) | https://doi.org/10.1002/mas.1280260109 |
| Comet (alternativa libre a SEQUEST) | https://comet-ms.sourceforge.io |
| UniProt (FASTA para búsqueda) | https://www.uniprot.org |

