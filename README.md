# DoctorML: Predicción de Riesgo Cardiovascular con Machine Learning

DoctorML es un modelo de aprendizaje automático que predice el riesgo de ataque cardiovascular a partir de datos clínicos de pacientes. Utiliza técnicas de clasificación supervisada para apoyar la toma de decisiones médicas en etapas tempranas, buscando contribuir con herramientas inteligentes al sector salud.

## Dataset

El modelo se entrena usando el dataset público **Cardio Train** del repositorio de análisis de salud cardiovascular, que incluye variables como:

- Edad
- Género
- Presión arterial (sistólica y diastólica)
- Colesterol
- Glucosa
- Tabaquismo
- Actividad física
- IMC
- Diagnóstico previo

Fuente: [Kaggle - Cardiovascular Disease Dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

## Tecnologías usadas

- Python 3
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

## Instalación

1. Clona este repositorio:
git clone [DoctorML-Modelo-Predictivo-de-Riesgo-Cardiovascular](https://github.com/LeoNato04/DoctorML-Modelo-Predictivo-de-Riesgo-Cardiovascular)
```bash
cd DoctorML
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
venv/bin/activate 
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Modelos entrenados

Se probaron y compararon los siguientes algoritmos:

- Regresión logística
- Árboles de decisión
- Random Forest
- XGBoost
- SVM (Support Vector Machine)

La selección final se basó en métricas como **accuracy**, **precision**, **recall**, y **F1-score**.

## Resultados

El mejor modelo alcanzó:

- Accuracy: 0.86
- F1-score: 0.84
- Interpretabilidad mediante matriz de confusión y curva ROC.

## Estructura del proyecto

<pre> ```text DoctorML/ ├── data/ │ └── cardio_train.csv ├── static/ │ ├── css/ │ ├── functions/ │ ├── graphics/ │ ├── images/ │ └── js/ ├── templates/ │ ├── contact.html │ ├── health.html │ ├── health_c_cardio.html │ ├── health_c_cardio_graphics.html │ ├── health_c_mama.html │ ├── health_c_pulmon.html │ ├── index.html │ ├── medicine.html │ └── news.html ├── app.py ├── requirements.txt └── README.md ``` </pre>

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.

## Autor
Leonel Fortunato Lizarbe Almeyda
Estudiante de Computación Científica – UNMSM
📧 leonel.lizarbe@unmsm.edu.pe
