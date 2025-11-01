# Peptidos

## InfoColumnas
### ¿Qué representa cada tipo de columna?

| Tipo de información | Nombre típico de columnas | ¿Qué significa? |
|---|---|---|
| **Identidad del péptido** | `Sequence` | Secuencia de aminoácidos del péptido. |
| **Características fisicoquímicas** | `Mass`, `Length`, `Charge`, `Missed cleavages` | Masa teórica, número de aminoácidos, carga observada y cortes de tripsina no realizados. |
| **Proteínas asociadas** | `Proteins`, `Leading razor protein`, `Protein group IDs` | Lista de proteínas posibles a las que pertenece el péptido; se usa para asignar proteínas después. |
| **Genes asociados** | `Gene names` | Nombre(s) del/los genes correspondientes. |
| **Validación / confianza** | `PEP`, `Score`, `Delta score` | Indicadores estadísticos de **confianza** en la identificación. PEP = probabilidad de error (cuanto menor, mejor). |
| **Control de calidad** | `Reverse`, `Potential contaminant` | Marcan identificaciones falsas de control (*Reverse*) o contaminantes (como queratina). Se eliminan en análisis reales. |
| **Cuantificación** | `Intensity A1`, `LFQ intensity A1`, etc. | Miden la **abundancia** del péptido en cada muestra. **LFQ** = valor normalizado para comparación entre muestras. |

---

## Columnas esenciales

### Qué contiene esta versión

Solo las columnas esenciales para una **primera interpretación**:

| Tipo | Columnas incluidas |
|---|---|
| **Identidad del péptido** | `Sequence` |
| **Relación péptido ↔ proteína** | `Proteins`, `Gene names` |
| **Confianza de identificación** | `PEP` |
| **Cuantificación por muestra** | Todas las columnas que empiezan por `Intensity` o `LFQ intensity` |

Esto permite trabajar conceptos clave **sin ruido** de columnas avanzadas.
