# funcions/cardio.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar y preprocesar el dataset
def cargar_modelo():
    df = pd.read_csv('data/cardio_train.csv', delimiter=';')
    df['age'] = (df['age'] / 365).astype(int)
    df = df[(df['ap_hi'] > 0) & (df['ap_lo'] > 0)]

    X = df[['age', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']]
    y = df['cardio']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")
    return model

modelo = cargar_modelo()

# Función para predecir el riesgo
def predecir_riesgo(edad, altura, peso, ap_hi, ap_lo, colesterol, glucosa, fuma, alco, activo):
    try:
        # Validar presión arterial
        if ap_hi < ap_lo:
            return {"error": "La presión sistólica (ap_hi) no puede ser menor que la diastólica (ap_lo)."}

        # Clasificar niveles de colesterol
        if colesterol < 200:
            colesterol = 1
        elif colesterol <= 239:
            colesterol = 2
        else:
            colesterol = 3
        
        # Clasificar niveles de glucosa
        if glucosa < 100:
            glucosa = 1
        elif glucosa <= 125:
            glucosa = 2
        else:
            glucosa = 3
        
        # Realizar predicción
        datos_usuario = [[edad, altura, peso, ap_hi, ap_lo, colesterol, glucosa, fuma, alco, activo]]
        probabilidad = modelo.predict_proba(datos_usuario)[0][1] * 100
        prediccion = modelo.predict(datos_usuario)[0]
        
        resultado = f"Tienes un riesgo de {probabilidad:.2f}% de enfermedad cardiovascular."
        if prediccion == 1:
            resultado += "\nEsto indica un alto riesgo. Te recomendamos consultar a un médico."
        else:
            resultado += "\nTu riesgo es bajo, pero igualmente, te recomendamos consultar a un médico. ¡Sigue cuidando tu salud!"
        
        return {"resultado": resultado}
    
    except ValueError:
        return {"error": "Por favor, ingresa valores numéricos válidos."}
