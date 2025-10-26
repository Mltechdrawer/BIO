# Epigenética

## Introducción: más allá de la secuencia del ADN  
La **epigenética** estudia los cambios heredables en la expresión génica que no implican alteraciones en la secuencia del ADN.  
Estos mecanismos permiten que células con el mismo genoma adopten funciones y fenotipos distintos.  
El concepto fue propuesto originalmente por **Conrad Waddington**, quien describió el “paisaje epigenético” para representar la capacidad de una célula de diferenciarse en múltiples destinos posibles.  
En términos metafóricos, si el ADN es el texto, la epigenética es la puntuación y el formato que determinan cómo se lee y cuándo se interpreta.  

---

## Fundamentos moleculares de la regulación epigenética  

### Metilación del ADN  
La **metilación del ADN** consiste en la adición de grupos metilo (–CH₃) sobre las citosinas en regiones CpG.  
Esta modificación química no altera la secuencia, pero **bloquea la unión de factores de transcripción** y suele asociarse con el **silenciamiento génico**.  
Las enzimas responsables son las **ADN metiltransferasas (DNMTs)**, entre ellas DNMT1, DNMT3A y DNMT3B.  
La metilación cumple funciones esenciales en el desarrollo embrionario, la impronta genómica y la inactivación del cromosoma X.  

### Modificaciones de histonas  
Las histonas, proteínas alrededor de las cuales se enrolla el ADN, pueden modificarse químicamente mediante **acetilación, metilación, fosforilación o ubiquitinación**.  
Estas marcas determinan el grado de compactación de la cromatina:  
- La **acetilación** generalmente **activa la transcripción**, relajando la estructura del ADN.  
- La **desacetilación** o ciertas metilaciones **la reprimen**, condensando la cromatina.  
El conjunto de estas marcas forma el llamado **“código de histonas”**, que regula la expresión génica de manera dinámica. 

#### Marcas epigenéticas de histonas y su interpretación

Las modificaciones químicas de las histonas no son aleatorias, sino que constituyen un lenguaje epigenético que informa sobre el estado funcional de los genes.  
Cada combinación de **residuo modificado (aminoácido)** y **tipo de modificación** (acetilación o metilación) se asocia a un resultado distinto sobre la expresión génica.  
Por convención, las marcas se nombran indicando la **histona (H3, H4, etc.)**, el **aminoácido** (por ejemplo, lisina *K*) y el **número de posición** dentro de la proteína.  

Algunos ejemplos relevantes:

- **H3K27ac (acetilación de la lisina 27 de la histona H3):**  
  Marca asociada a **activación transcripcional**. Se localiza en **promotores activos** y especialmente en **enhancers activos**.  

  <details>
  <summary> H3K27ac - Enhancers activos</summary>
   <p>Ejemplo: región del enhancer del gen MYC (cromosoma 8 en humanos).</p>
   <p>En los datos de ENCODE, esta región muestra un pico intenso de H3K27ac en células activamente proliferantes (como líneas HeLa o K562).</p>
   <p>Interpretación: la presencia de H3K27ac en enhancers indica que el enhancer está activo y contribuye a la transcripción del gen MYC, un oncogén cuya expresión depende fuertemente del estado epigenético.</p>
   <p> <strong>Visualización sugerida: </strong> En UCSC Genome Browser -> activar las pistas (tracks) de ENCODE Histone Modification → seleccionar H3K27ac en la región del gen MYC.</p>
  </details>

- **H3K27me3 (trimetilación de la lisina 27 de H3):**  
  Marca clásica de **represión génica** mediada por el complejo **Polycomb (PRC2)**. Define regiones de cromatina compacta e inactiva.

  <details>
  <summary> H3K27me3 - Represión génica mediada por Polycomb</summary>
   <p>Ejemplo: gen HOXA9, perteneciente al clúster HOX en el cromosoma 7.</p>
   <p>En células madre embrionarias (hESCs), esta región presenta una amplia marca de H3K27me3, lo que mantiene al gen reprimido.</p>
   <p>Al diferenciarse las células, la marca se elimina y el gen se activa en tejidos donde es necesario para el desarrollo.</p>
   <p> <strong>Interpretación: </strong> H3K27me3 mantiene genes de desarrollo silenciados hasta que se activan mediante remodelado epigenético.</p>
  </details>

- **H3K4me3 (trimetilación de la lisina 4 de H3):**  
  Marca de **promotores activos**. Se concentra en el **TSS (sitio de inicio de la transcripción)** y su intensidad refleja el **grado de actividad** de un gen.

  <details>
  <summary> H3K4me3 — Promotores activos</summary>
   <p>Ejemplo: gen GAPDH (enzima de la glicólisis, altamente expresada)</p>
   <p>En casi todas las líneas celulares humanas, el TSS (sitio de inicio de transcripción) de GAPDH presenta un pico agudo de H3K4me3.</p>
   <p>Este patrón es característico de promotores activos de genes “housekeeping”.</p>
   <p> <strong>Visualización sugerida: </strong> En el navegador genómico de UCSC o en IGV, visualizar H3K4me3 en la región promotora de GAPDH.</p>
  </details>

- **H3K36me3 (trimetilación de la lisina 36 de H3):**  
  Asociada a **transcripción elongada**; aparece en el **cuerpo de los genes activamente transcritos**. 

  <details>
  <summary> H3K36me3 — Genes activamente transcritos</summary>
   <p>Ejemplo: el gen ACTB (β-actina), otro gen constitutivo.</p>
   <p>Presenta una fuerte señal de H3K36me3 a lo largo de todo su cuerpo génico, especialmente en la región distal.</p>
   <p> <strong>Interpretación: </strong> Esta marca indica elongación activa de la transcripción y está asociada a genes expresados de forma estable.</p>
  </details>

- **H3K9me3 (trimetilación de la lisina 9 de H3):**  
  Marca de **heterocromatina constitutiva** y **silenciamiento estable** de genes y regiones repetitivas.

  <details>
  <summary> H3K9me3 — Heterocromatina y silenciamiento estable</summary>
   <p>Ejemplo: regiones pericentroméricas o teloméricas del genoma (por ejemplo, en el cromosoma 1).</p>
   <p>Estas regiones muestran altos niveles de H3K9me3 y ausencia de marcas activadoras.</p>
   <p> <strong>Interpretación: </strong> Es una marca de heterocromatina constitutiva, típica de regiones repetitivas no transcritas.</p>
  </details>

Estas combinaciones de marcas conforman el denominado **“código de histonas”**, que actúa como un sistema de señalización dinámico que puede ser leído por proteínas específicas para activar, mantener o reprimir la expresión génica.

### microARNs (miRNAs) y control post-transcripcional  
Los **microARNs (miRNAs)** son pequeñas moléculas de ARN no codificante (~22 nucleótidos) que se unen de forma complementaria a los **ARN mensajeros (mRNA)**.  
Su acción impide la traducción del mRNA o promueve su degradación, modulando la **expresión génica post-transcripcional**.  
Este mecanismo permite un control fino y reversible de la producción de proteínas, y es fundamental en procesos como el desarrollo, la diferenciación celular o la respuesta al estrés.  

---

![Regulación Epigenética](B103/epigenetica.png "Regulación Epigenética")

*Regulación Epigenética*

---

<details>
<summary> Detalles</summary>
<p>El estudio de estos mecanismos es conocido como epigenética. Se realiza colocando moléculas químicas en zonas muy concretas de la molécula de ADN que facilita que los genes se activen o desactiven.</p>
<p>Son marcas químicas que cambian la forma en la que se lee el ADN, pero sin alterar su secuencia, que sigue siendo la misma.</p>
<p>Por ejemplo, imagina la frase: </p>
<p>No está mal el resultado</p>
<p>No. Está mal el resultado</p>
<p>¡No! Está mal el resultado</p>
</details>

---

## Herencia epigenética y reprogramación celular  
- Las marcas epigenéticas pueden **transmitirse durante la división celular**, manteniendo la identidad funcional.  
- En etapas tempranas del desarrollo embrionario, ocurre una **reprogramación epigenética global** que borra y restablece estas marcas.  
- Se ha descrito **herencia epigenética transgeneracional**, donde ciertas modificaciones persisten entre generaciones sin alterar el ADN.  

---

## Epigenética y expresión génica  
La epigenética actúa como un nivel adicional de regulación sobre el genoma.  
Las marcas epigenéticas determinan qué regiones del ADN son accesibles a los **factores de transcripción** y, por tanto, si un gen se expresa o se mantiene silenciado.  
Los **ARN no codificantes**, como los microARN y lncRNA, también participan en esta regulación, estableciendo circuitos epigenéticos complejos.  

---

## Herramientas y tecnologías en epigenómica  

### Técnicas experimentales  
- **Bisulfite sequencing (BS-seq):** analiza la metilación del ADN a nivel de nucleótido.  
- **ChIP-seq:** identifica regiones de unión de proteínas, histonas modificadas o factores de transcripción.  
- **ATAC-seq y DNase-seq:** evalúan la accesibilidad de la cromatina.  

### Análisis bioinformático  
- Procesamiento de datos de metilación y enriquecimiento de regiones reguladoras.  
- Integración multi-ómica entre metilación, histonas y expresión génica.  
- Bases de datos epigenómicas relevantes: **ENCODE**, **Roadmap Epigenomics**, **GEO**.  

---

## Aplicaciones biomédicas de la epigenética  
- **Epigenética del cáncer:** hipometilación global y silenciamiento de genes supresores de tumores.  
- **Epigenética del envejecimiento:** aparición de los llamados “**relojes epigenéticos**” (Horvath clock).  
- **Terapias epigenéticas:** inhibidores de DNMT y HDAC como tratamientos antitumorales.  
- **Nutriepigenómica y ambiente:** cómo factores externos como dieta o estrés influyen en el epigenoma.  

---

## Epigenética computacional y ciencia de datos  
- Aplicación de **machine learning** para predecir patrones epigenéticos y regiones reguladoras activas.  
- Integración de datos epigenómicos en modelos multi-ómicos para inferir redes de regulación génica.  
- Visualización de marcas epigenéticas en **browsers genómicos** como UCSC Genome Browser o IGV.  

---

## Perspectivas futuras  
- **Single-cell epigenomics:** permite analizar la variabilidad epigenética entre células individuales.  
- **Edición epigenética:** uso de CRISPR-dCas9 fusionado a enzimas epigenéticas para modificar metilaciones o acetilaciones específicas.  
- Consideraciones éticas sobre la manipulación epigenética y su posible herencia transgeneracional.  

---

## Conclusión  
La epigenética amplía la genética clásica al incorporar un nivel de regulación dinámico, reversible y sensible al entorno.  
Su integración con la bioinformática y la ciencia de datos está revelando cómo el epigenoma conecta el ambiente con la función celular, aportando claves esenciales para la medicina personalizada y la biología de sistemas.  

---

[Actividad 1](actividad_visualizacionepigenetica1.md "Actividad 1")

[Actividad 2](actividad_visualizacionepigenetica2.md "Actividad 2")

