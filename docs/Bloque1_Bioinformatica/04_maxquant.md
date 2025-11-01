# MaxQuant

**MaxQuant** es una plataforma de análisis de datos de **proteómica basada en espectrometría de masas**, ampliamente utilizada para la **identificación y cuantificación** de proteínas. Incluye de forma nativa el motor de búsqueda **Andromeda**, que realiza la identificación de péptidos, y ofrece herramientas avanzadas para el **control de FDR**, **normalización**, **cuantificación basada en intensidad (LFQ)** y análisis de modificaciones postraduccionales.

MaxQuant se emplea tanto en **investigación académica** como en laboratorios de proteómica clínica y estructural. Permite la integración con herramientas de análisis posteriores como **Perseus**.

---

### ¿Para qué se usa MaxQuant?

MaxQuant permite:

- Identificar **péptidos y proteínas** a partir de datos MS/MS.
- Realizar **cuantificación proteica**, incluyendo:
  - **LFQ (Label-Free Quantification)**
  - **iBAQ (Intensity-Based Absolute Quantification)**
- Detectar y analizar **modificaciones postraduccionales** (ej. fosforilación, acetilación).
- Aplicar filtros estadísticos rigurosos mediante **FDR controlado** a nivel de péptido y proteína.
- Generar archivos estructurados para análisis posteriores.

---

### ¿Cómo se usa MaxQuant?

1. **Descargar e instalar**
   - https://www.maxquant.org  
   - Ejecutable para Windows / Linux (Mono).

2. **Preparar los datos**
   - Archivos brutos `.raw` de espectrómetros Thermo u otros convertidos a `.mzML`.
   - Base de datos FASTA curada (ej. UniProt):
     https://www.uniprot.org

3. **Configurar el proyecto**
   - Abrir `MaxQuant.exe`.
   - En *Global Parameters*:
     - Seleccionar la base de datos FASTA.
   - En *Group-Specific Parameters*:
     - **Enzima:** Trypsin/P
     - **Tolerancia de masa:** precursors 20 ppm; fragmentos 0.5–0.8 Da (dependiendo del análisis)
     - **Modificaciones fijas:** Carbamidometilación (C)
     - **Modificaciones variables:** Oxidación (M), Fosforilación (S/T/Y) si procede

4. **Ejecutar**
   - MaxQuant ejecutará **Andromeda** para la identificación y aplicará cuantificación y filtrado automático.

5. **Interpretar resultados**
   - Archivos clave:
     - `proteinGroups.txt` → lista final de proteínas
     - `peptides.txt` → péptidos identificados
     - `evidence.txt` → evidencia a nivel de espectro
   - Se recomienda análisis estadístico con **Perseus** o scripts en **R/Python**.

---

### Resumen

**MaxQuant es una plataforma completa para identificación y cuantificación de proteínas que integra el motor Andromeda y herramientas robustas de control estadístico y cuantificación LFQ.**

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial MaxQuant | https://www.maxquant.org |
| Descargas | https://www.maxquant.org/download_asset/maxquant |
| Documentación | https://www.maxquant.org/documentation |
| Perseus (análisis downstream) | https://www.maxquant.org/perseus |
| Publicación original MaxQuant (Cox & Mann, 2008, *Nature Biotechnology*) | https://doi.org/10.1038/nbt.1511 |
| Publicación original Andromeda (Cox et al., 2011, *MCP*) | https://doi.org/10.1074/mcp.M111.014985 |
| UniProt (bases FASTA) | https://www.uniprot.org |

