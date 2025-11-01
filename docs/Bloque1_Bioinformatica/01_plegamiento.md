# Plegamiento de proteínas

El **plegamiento de proteínas** es el proceso mediante el cual una **cadena lineal de aminoácidos** (estructura primaria) adopta una **conformación tridimensional específica y funcional**.  
Esta conformación final, denominada **estructura nativa**, es esencial para que la proteína realice su función biológica correctamente.  
El estudio del plegamiento constituye una de las áreas más fascinantes de la biología molecular y la bioinformática, ya que conecta la **secuencia**, la **estructura** y la **función** de las proteínas.

---

## Introducción

Cada proteína recién sintetizada emerge del ribosoma como una **cadena polipeptídica lineal**.  
Sin embargo, en milisegundos o segundos, esa cadena se **autoensambla espontáneamente** hasta alcanzar una estructura tridimensional altamente específica.  
Este proceso depende de interacciones químicas internas y del entorno celular.  

El plegamiento correcto es vital:  
una proteína mal plegada puede **perder su función**, **agregarse** o incluso **provocar enfermedades**.  
Por ello, las células poseen mecanismos especializados —las **chaperonas moleculares**— que supervisan y corrigen el plegamiento.

---

## Fundamentos del plegamiento proteico

El plegamiento es un proceso **termodinámico** impulsado por la búsqueda del **estado de menor energía libre (ΔG)**.  
La proteína explora múltiples conformaciones posibles hasta alcanzar su forma más estable, conocida como **conformación nativa**.

### Fuerzas que dirigen el plegamiento
- **Interacciones hidrofóbicas:** los aminoácidos no polares se agrupan en el interior, evitando el contacto con el agua.  
- **Puentes de hidrógeno:** estabilizan las hélices alfa y láminas beta.  
- **Interacciones iónicas:** entre grupos cargados positiva y negativamente.  
- **Fuerzas de Van der Waals:** contribuyen al empaquetamiento fino del núcleo hidrofóbico.  
- **Puentes disulfuro:** enlaces covalentes entre residuos de cisteína que refuerzan la estabilidad estructural.

### El modelo del embudo de energía
El **modelo del embudo energético** describe el proceso como una búsqueda guiada:  
la proteína comienza en un estado de alta energía y desorden, y va descendiendo por el “embudo” hasta alcanzar el mínimo global de energía correspondiente a su estructura nativa.  
Aunque existen miles de posibles conformaciones, las restricciones químicas y energéticas reducen drásticamente el espacio de búsqueda.

---

## Vías y modelos de plegamiento

### Modelo jerárquico
El plegamiento ocurre en etapas sucesivas:
1. Formación de **estructuras secundarias** locales (hélices α, láminas β).  
2. Asociación de estas estructuras en **dominios**.  
3. Compactación global hacia la estructura terciaria.

### Modelo de nucleación
Algunas regiones estables actúan como **núcleos de plegamiento**, atrayendo el resto de la cadena hacia la estructura final.

### Dilema de Levinthal
Cyrus Levinthal (1969) planteó que una proteína no puede probar todas las conformaciones posibles al azar:  
si lo hiciera, tardaría más que la edad del universo en plegarse.  
Esto demuestra que el plegamiento **no es aleatorio**, sino que sigue **rutas energéticamente favorables**.

---

## Chaperonas moleculares

Las **chaperonas** son proteínas que **asisten el plegamiento de otras proteínas** sin formar parte de su estructura final.  
Evitan interacciones erróneas, agregación y desnaturalización.

### Tipos principales
- **Hsp70 y Hsp90:** reconocen regiones hidrofóbicas expuestas en proteínas parcialmente plegadas.  
- **Chaperoninas (GroEL/GroES):** complejos cilíndricos que proporcionan un microambiente aislado para el plegamiento correcto.  
- **Pequeñas Hsps:** actúan como “guardianes” frente al estrés térmico.

### Mecanismo de acción
Las chaperonas utilizan **ATP** para inducir cambios conformacionales que ayudan a las proteínas clientes a alcanzar su forma nativa.  
Su función es crítica durante el estrés celular, cuando el calor o la oxidación pueden provocar mal plegamiento.

---

## Desnaturalización y replegamiento

### Desnaturalización
Ocurre cuando una proteína pierde su estructura tridimensional sin romper los enlaces peptídicos de la secuencia.  
Puede ser causada por:
- Calor excesivo.  
- pH extremo.  
- Agentes químicos (urea, guanidina).  
- Solventes orgánicos.

El resultado es la **pérdida de función biológica**.

### Replegamiento
En muchos casos, la desnaturalización es **reversible** si se restauran las condiciones originales.  
El **experimento clásico de Anfinsen (1973)** con la **ribonucleasa A** demostró que toda la información necesaria para el plegamiento reside en la **secuencia de aminoácidos**, no en factores externos.

---

## Mal plegamiento y enfermedades conformacionales

Cuando el plegamiento falla, las proteínas pueden:
- Permanecer **no funcionales**.  
- Formar **agregados insolubles**.  
- Generar **fibrillas amiloides** tóxicas para las células.

### Ejemplos de enfermedades relacionadas
| Enfermedad | Proteína afectada | Consecuencia |
|-------------|------------------|---------------|
| **Alzheimer** | β-amiloide y tau | Formación de placas y ovillos neurofibrilares |
| **Parkinson** | α-sinucleína | Agregados citoplasmáticos (cuerpos de Lewy) |
| **Prionopatías** | PrP | Conversión de conformación normal a patológica |
| **Fibrosis quística** | CFTR | Mal plegamiento y degradación prematura de la proteína |

Las células disponen de sistemas de control de calidad como el **sistema ubiquitina-proteasoma** o la **autofagia** para eliminar proteínas mal plegadas.

---

## Predicción y modelado computacional del plegamiento

El **problema del plegamiento de proteínas** ha sido uno de los mayores retos de la bioinformática estructural.

### Métodos computacionales
1. **Modelado por homología:** predice la estructura basándose en proteínas con secuencias similares conocidas (SWISS-MODEL, MODELLER).  
2. **Métodos *ab initio*:** simulan el plegamiento desde cero, sin plantilla (Rosetta, QUARK).  
3. **Dinámica molecular (MD):** analiza el movimiento atómico en escalas temporales (GROMACS, NAMD).  
4. **AlphaFold (DeepMind, 2021):** red neuronal profunda que predice estructuras con precisión experimental.  

### Evaluación de la calidad estructural
- **RMSD (Root Mean Square Deviation)** → mide la desviación promedio entre estructuras.  
- **TM-score** → evalúa la similitud global de la topología.  
- **pLDDT (AlphaFold)** → indica la confianza en cada región de la predicción.

---

## Relevancia bioinformática y en ciencia de datos

El plegamiento proteico se ha convertido en un **problema computacional de alto impacto**.  
La aplicación de modelos de **machine learning** ha revolucionado el campo.

### Áreas de aplicación
- **Predicción de estabilidad** ante mutaciones (DeepDDG, FoldX).  
- **Identificación de sitios activos o de unión a ligandos.**  
- **Análisis de redes de contacto** y dinámicas de plegamiento mediante grafos.  
- **Diseño de proteínas (protein design)** → ingeniería de nuevas funciones o estructuras artificiales.

Los avances en IA, aprendizaje profundo y GPUs han hecho posible modelar **millones de proteínas** con un nivel de detalle antes inimaginable.

---

## Ejemplo práctico: visualización del plegamiento

**Objetivo:** observar cómo una proteína adquiere su estructura tridimensional.  

1. Accede al **Protein Data Bank (PDB):** [https://www.rcsb.org](https://www.rcsb.org)  
2. Busca la estructura **ribonucleasa A (PDB: 7RSA)**.  
3. Descarga el archivo `.pdb` y ábrelo con **UCSF ChimeraX** o **Mol\***.  
4. Identifica:
   - Hélices alfa y láminas beta.  
   - Regiones hidrofóbicas internas.  
   - Puentes disulfuro.  
5. Opcional: compara la estructura experimental con la predicha por **AlphaFold**.

**Reflexión:** ¿qué diferencias observas entre la estructura teórica y la experimental?  
¿Cómo se refleja la estabilidad en la disposición del núcleo hidrofóbico?

---

## Conclusiones

- El **plegamiento proteico** traduce la información genética en estructura funcional.  
- La secuencia de aminoácidos **contiene toda la información necesaria** para el plegamiento correcto.  
- Las **chaperonas** y mecanismos de control celular aseguran la estabilidad del proteoma.  
- Los fallos en este proceso se asocian a **enfermedades neurodegenerativas** y a pérdida funcional.  
- La **bioinformática estructural** y la **inteligencia artificial** han permitido modelar el plegamiento con una precisión sin precedentes.


[AlphaFold](01_alphafold.md "AlphaFold")


