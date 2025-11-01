# Andromeda

La *search engine* **Andromeda** es el motor de identificación de péptidos integrado dentro de **MaxQuant**, uno de los softwares más utilizados en proteómica basada en espectrometría de masas. Andromeda **no se usa de forma independiente normalmente**, sino que trabaja embebido en MaxQuant para comparar espectros MS/MS con bases de datos de proteínas.

---

### ¿Para qué sirve Andromeda?

Sirve para:

- Buscar **qué péptidos** corresponden a los espectros MS/MS.
- Permitir identificar **proteínas** a partir de los péptidos detectados.
- Aplicar reglas de **modificaciones**, **enzimas de digestión**, **tolerancias de masas**, etc.

Funciona comparando los espectros experimentales con espectros teóricos generados a partir de una base de datos FASTA. Utiliza un sistema de **scoring probabilístico** derivado del algoritmo *Andromeda Score*.

---

### ¿Cómo se usa Andromeda dentro de MaxQuant?

1. **Descargar MaxQuant**
   - Web oficial: https://www.maxquant.org
   - Versión recomendada: última estable

2. **Preparar tus datos**
   - Archivos RAW (Thermo) o convertidos (mzML).
   - Base de datos FASTA (ej. UniProt): https://www.uniprot.org

3. **Configurar el análisis en MaxQuant**
   - Abre `MaxQuant.exe`
   - En la pestaña **Global Parameters**:
     - Selecciona la base de datos FASTA.
   - En **Group-specific parameters**:
     - Configurar:
       - **Enzima:** *Trypsin/P*
       - **Tolerancia de masa:** precursos → 20 ppm, fragmentos → 0.5 Da
       - **Modificaciones fijas:** Carbamidometilación de Cys
       - **Modificaciones variables:** Oxidación de Met

4. **Ejecutar**
   - MaxQuant llamará automáticamente a **Andromeda** durante la fase de búsqueda de péptidos.

5. **Resultados**
   - Archivos clave:
     - `peptides.txt`
     - `proteinGroups.txt`
   - Se visualizan y analizan frecuentemente en:
     - **Perseus** → https://maxquant.org/perseus
     - Scripts en **R** o **Python**

---

### Resumen

**Andromeda no se usa sola**, sino integrada en **MaxQuant**, donde realiza la búsqueda de péptidos comparando espectros MS/MS con bases de datos proteicas y aplicando control de FDR.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial MaxQuant (incluye Andromeda) | https://www.maxquant.org |
| Repositorio / Descargas de MaxQuant | https://www.maxquant.org/download_asset/maxquant |
| Documentación y tutoriales de MaxQuant | https://www.maxquant.org/documentation |
| UniProt (descarga de bases FASTA) | https://www.uniprot.org |
| Publicación original de Andromeda (Cox et al., 2011, *Molecular & Cellular Proteomics*) | https://doi.org/10.1074/mcp.M111.014985 |
| Publicación de MaxQuant (Cox & Mann, 2008, *Nature Biotechnology*) | https://doi.org/10.1038/nbt.1511 |
| Perseus (software para análisis downstream) | https://www.maxquant.org/perseus |
