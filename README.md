# 📶 Predictor de tecnología de acceso a Internet Fijo (Colombia)

Proyecto Integrador — **Aprendizaje de Máquinas** · Metodología **CRISP-DM**.

Aplicación web que predice la **tecnología de acceso a internet fijo**
(Fibra óptica, Cable, HFC, DSL o Inalámbrica) de una conexión, a partir de su
departamento, segmento socioeconómico y velocidades de bajada/subida.

## 🎯 El problema
Clasificación multiclase. El modelo aprende de los datos oficiales de la
Comisión de Regulación de Comunicaciones publicados en **Datos Abiertos Colombia**
(*Internet Fijo Accesos por tecnología y segmento*, id `n48w-gutb`).

## 🧠 Modelo
- Pipeline de scikit-learn: `OneHotEncoder` + imputación/escalado + **Árbol de
  Decisión ajustado** (`max_depth=15`), con balanceo **SMOTE** en entrenamiento.
- Desempeño en prueba: **Accuracy ≈ 0.78 · F1-macro ≈ 0.74**.
- Todo el preprocesamiento va dentro del pipeline serializado (`pipeline.pkl`).

## 📂 Archivos
| Archivo | Descripción |
|---|---|
| `app.py` | Aplicación Streamlit |
| `pipeline.pkl` | Pipeline completo serializado (preprocesamiento + modelo) |
| `opciones.pkl` | Valores válidos para los menús de la app |
| `requirements.txt` | Dependencias con versiones fijadas |

## ▶️ Ejecutar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```
La app se abre en `http://localhost:8501`.

## ☁️ Despliegue
Desplegada en **Streamlit Community Cloud** conectando este repositorio de GitHub.

---
*El cuaderno completo con las 6 fases de CRISP-DM está en el repositorio del proyecto.*
