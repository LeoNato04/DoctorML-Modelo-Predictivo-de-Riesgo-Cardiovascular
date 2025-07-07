# funcions/cancerpulmon.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar y preprocesar el dataset
def cargar_modelo():
    df = pd.read_csv(r'C:\Users\casa\Documents\UNIVERSIDAD\VERANO 2025-0\IA\PROYECTO FINAL\Doctor_ML\data\Lung Cancer dataset.csv')

    # Convertir columnas relevantes a tipo entero
    df['AGE'] = df['AGE'].astype(int)

    # Definir las características (X) y la variable objetivo (y)
    X = df[['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE', 
            'CHRONIC_DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 
            'ALCOHOL_CONSUMING', 'COUGHING', 'SHORTNESS_OF_BREATH', 
            'SWALLOWING_DIFFICULTY', 'CHEST_PAIN']]
    y = df['LUNG_CANCER'].apply(lambda x: 1 if x == 'YES' else 0)  # Convertir a binario

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Crear y entrenar el modelo
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")
    return model

modelo = cargar_modelo()

# Función para predecir el riesgo
def predecir_riesgo(genero, edad, fumar, dedos_amarillos, ansiedad, presion_companeros, 
                    enfermedad_cronica, fatiga, alergia, sibilancias, 
                    consumo_alcohol, tos, dificultad_respirar, dificultad_tragar, dolor_pecho):
    try:
        # Convertir género a valor numérico
        if genero.upper() == 'M':
            genero = 1
        elif genero.upper() == 'F':
            genero = 0
        else:
            return {"error": "Género no válido. Usa 'M' para masculino o 'F' para femenino."}

        # Datos del usuario para la predicción
        datos_usuario = [[genero, edad, fumar, dedos_amarillos, ansiedad, presion_companeros, 
                          enfermedad_cronica, fatiga, alergia, sibilancias, 
                          consumo_alcohol, tos, dificultad_respirar, 
                          dificultad_tragar, dolor_pecho]]
        
        # Obtener probabilidad de riesgo
        probabilidad = modelo.predict_proba(datos_usuario)[0][1] * 100
        prediccion = modelo.predict(datos_usuario)[0]
        
        resultado = f"Tienes un riesgo de {probabilidad:.2f}% de cáncer de pulmón."
        if prediccion == 1:
            resultado += "\nEsto indica un alto riesgo. Te recomendamos consultar a un médico."
        else:
            resultado += "\nTu riesgo es bajo. ¡Sigue cuidando tu salud!"
        
        return {"resultado": resultado}
    
    except ValueError:
        return {"error": "Por favor, ingresa valores numéricos válidos."}