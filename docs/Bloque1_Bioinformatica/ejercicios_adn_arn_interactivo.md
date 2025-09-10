# Ejercicios: Detecta el fallo en la secuencia

## 1. Base prohibida en el ARN
**Enunciado:**  
```
5' – AUGCUATGC – 3'
```
**Pregunta:** ¿Qué error contiene y cómo lo corregirías?  

<details>
  <summary>💡 Ver solución</summary>

El ARN nunca contiene timina (T). La base correcta es uracilo (U).  
La secuencia corregida sería:  
```
5' – AUGCUAUGC – 3'
```

</details>

---

## 2. Complementariedad incorrecta en ADN
**Enunciado:**  
Secuencia de ADN (hebra 1):  
```
5' – ATGCCGTA – 3'
```  
Hebra complementaria propuesta:  
```
3' – TACGGCAT – 5'
```  
**Pregunta:** ¿Es correcta la complementariedad?  

<details>
  <summary>💡 Ver solución</summary>

Sí, es correcta. Cada A está emparejada con T y cada G con C.  
La complementariedad es adecuada, manteniendo el antiparalelismo.  

</details>

---

## 3. Orientación invertida
**Enunciado:**  
Supuesta doble hélice:  
```
Hebra 1: 5' – AGCTTAGC – 3'  
Hebra 2: 5' – TCGAATCG – 3'
```  
**Pregunta:** ¿Cuál es el error?  

<details>
  <summary>💡 Ver solución</summary>

Las hebras deben ser antiparalelas. La hebra 2 debería estar escrita como:  
```
3' – TCGAATCG – 5'
```  

</details>

---

## 4. Secuencia híbrida imposible
**Enunciado:**  
Secuencia dada:  
```
5' – AUGTCCGA – 3'
```  
**Pregunta:** ¿Qué incoherencia hay?  

<details>
  <summary>💡 Ver solución</summary>

La secuencia mezcla nucleótidos de ARN (U) con timina (T), que solo aparece en ADN.  
Debe escribirse todo en ADN (con T, sin U) o todo en ARN (con U, sin T).  

</details>

---

## 5. Uracilo en ADN
**Enunciado:**  
Secuencia de ADN propuesta:  
```
5' – ATGCUAGC – 3'
```  
**Pregunta:** ¿Cuál es el error en esta cadena?  

<details>
  <summary>💡 Ver solución</summary>

El ADN nunca contiene uracilo (U). En su lugar debe estar timina (T).  
La secuencia corregida sería:  
```
5' – ATGCTAGC – 3'
```  

</details>
