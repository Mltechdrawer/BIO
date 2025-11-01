# Skyline

**Skyline** es una plataforma **gratuita y de código abierto** diseñada para el **análisis cuantitativo de datos de proteómica y metabolómica** obtenidos mediante espectrometría de masas. Está desarrollada por la Universidad de Washington y es ampliamente utilizada para **cuantificación dirigida** en experimentos **SRM/MRM (triple cuadrupolo)** y **PRM (Orbitrap / Q-TOF)**, aunque también permite análisis de **cuantificación no dirigida (DIA/SWATH)**.

Skyline proporciona herramientas gráficas intuitivas para construir métodos, visualizar cromatogramas, integrar picos y comparar cuantificaciones entre muestras.

---

### ¿Para qué se usa Skyline?

Skyline permite:

- **Diseñar ensayos de cuantificación dirigida**, seleccionando péptidos diana.
- Importar datos MS de múltiples fabricantes (Thermo, Sciex, Waters, Bruker, Agilent…).
- Visualizar **cromatogramas extraídos (XICs)** y **curvas de calibración**.
- Realizar **cuantificación absoluta** (si hay estándar isotópico) o **cuantificación relativa**.
- Analizar datos de:
  - **SRM/MRM**
  - **PRM**
  - **DIA / SWATH**
  - **DDA** para selección inicial de targets

---

### ¿Cómo se usa Skyline?

1. **Instalación**
   - Descargar desde:  
     https://skyline.ms

2. **Configurar un documento**
   - Elegir **tipo de instrumento** (Orbitrap, QqQ, TOF, etc.)
   - Importar:
     - Lista de péptidos diana
     - Secuencia FASTA
     - Transiciones (si SRM/MRM)

3. **Importar datos de espectrometría**
   - Archivos `.raw`, `.mzML`, `.wiff`, `.d`, etc.

4. **Visualización y análisis**
   - Skyline extrae los **cromatogramas** correspondientes.
   - Se realiza la **integración manual o automática de picos**.
   - Se pueden generar:
     - **Curvas de calibración**
     - **Gráficas de cuantificación**
     - Informes exportables

5. **Exportación de resultados**
   - A Excel, `.csv`, o herramientas estadísticas externas (R / Python).

---

### Resumen

**Skyline es una herramienta clave para la cuantificación dirigida** en proteómica, permitiendo diseñar ensayos SRM/MRM y PRM, visualizar cromatogramas y realizar cuantificación absoluta o relativa usando una interfaz clara y flexible.

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Página oficial de Skyline | https://skyline.ms |
| Descarga directa | https://skyline.ms/project/home/software/Skyline/begin.view |
| Tutoriales oficiales | https://skyline.ms/wiki/home/software/Skyline/page.view?name=tutorials |
| Conjunto de prácticas docente *Skyline Tutorials* | https://skyline.ms/skyts/home/software/Skyline/page.view?name=workshop |
| Publicación (MacLean et al., 2010, *Bioinformatics*) | https://doi.org/10.1093/bioinformatics/btq054 |


