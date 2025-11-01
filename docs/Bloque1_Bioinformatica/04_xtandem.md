# X!Tandem

**X!Tandem** es una *search engine* de código abierto diseñada para la **identificación de péptidos** a partir de espectros MS/MS. Forma parte del conjunto de herramientas **X!Tandem Pipeline / Trans-Proteomic Pipeline (TPP)** y se utiliza ampliamente debido a su **carácter gratuito**, **flexibilidad** y la posibilidad de ejecutarse tanto en ordenadores personales como en clústeres de alto rendimiento.

---

### ¿Para qué sirve X!Tandem?

X!Tandem se emplea para:

- Identificar **péptidos** comparando espectros MS/MS experimentales con espectros teóricos generados a partir de bases de datos proteicas.
- Inferir **proteínas** a partir de los péptidos detectados.
- Aplicar reglas de **modificaciones fijas y variables**, **enzimas de corte**, **tolerancias de masas** y estrategias de búsqueda iterativa.
- Integrarse con **herramientas de validación de FDR** y estadística (como **PeptideProphet** dentro del TPP).

Su algoritmo evalúa la coincidencia entre espectros considerando **la intensidad de picos** y relaciones entre fragmentos para generar un **E-value**, indicador de confianza.

---

### ¿Cómo se usa X!Tandem?

1. **Descarga e instalación**
   - Descarga desde GitHub:  
     https://github.com/rkimmel/x-tandem  
   - Alternativamente, utilizar dentro de **TPP (Trans-Proteomic Pipeline)**:  
     https://www.tppms.org

2. **Preparar los datos**
   - Archivos MS/MS: `.mzML`, `.mgf`, `.raw` (convertidos previamente).
   - Base de datos proteica FASTA (ej. UniProt):  
     https://www.uniprot.org

3. **Configurar la búsqueda**
   - X!Tandem utiliza un archivo de configuración `.xml` donde se definen:
     - **Enzima** (ej. *trypsin*)
     - **Tolerancia de masa de precursor** (ej. 10–20 ppm)
     - **Tolerancia de masa de fragmentos** (ej. 0.5–0.8 Da)
     - **Modificaciones fijas:** Carbamidometilación de C
     - **Modificaciones variables:** Oxidación de M, Fosforilación (S/T/Y), etc.
   - Se puede ejecutar desde línea de comandos o mediante interfaz gráfica en TPP.

4. **Ejecutar**
   - X!Tandem produce un archivo de resultados `.xml` con puntuaciones y E-values.

5. **Validar y analizar resultados**
   - Comúnmente procesado con **PeptideProphet / ProteinProphet** para aplicar **FDR ≤ 1%**.
   - Resultados finales:
     - Lista de péptidos identificados
     - Proteínas inferidas
     - Probabilidades y métricas de calidad de identificación

---

### Resumen

**X!Tandem es una search engine abierta y flexible** para identificación de péptidos, frecuentemente usada dentro del **Trans-Proteomic Pipeline**, con resultados validados mediante estadística bayesiana (PeptideProphet / ProteinProphet).

---

### Fuentes recomendadas

| Recurso | URL |
|--------|-----|
| Repositorio X!Tandem | https://github.com/rkimmel/x-tandem |
| Trans-Proteomic Pipeline (TPP) | https://www.tppms.org |
| UniProt (bases FASTA) | https://www.uniprot.org |
| Publicación original de X!Tandem (Craig & Beavis, 2004) | https://doi.org/10.1093/bioinformatics/bth092 |

