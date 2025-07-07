from flask import Flask, render_template, request, redirect, url_for, flash
from static.functions.cardio import predecir_riesgo

app = Flask(__name__)
app.secret_key = 'super_secreto'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/medicina')
def medicina():
    return render_template('medicine.html')

@app.route('/cardio', methods=['GET', 'POST'])
def cardio():
    if request.method == 'POST':
        # Obtener datos del formulario
        edad = int(request.form.get('age'))
        altura = int(request.form.get('height'))
        peso = int(request.form.get('weight'))
        ap_hi = int(request.form.get('ap_hi'))
        ap_lo = int(request.form.get('ap_lo'))
        colesterol = int(request.form.get('cholesterol'))
        glucosa = int(request.form.get('gluc'))

        # Convertir opciones de Sí/No a 1/0
        fuma = 1 if request.form.get('smoke') == 'Sí' else 0
        alco = 1 if request.form.get('alco') == 'Sí' else 0
        activo = 1 if request.form.get('active') == 'Sí' else 0

        # Llamar a la función de predicción
        resultado = predecir_riesgo(edad, altura, peso, ap_hi, ap_lo, colesterol, glucosa, fuma, alco, activo)

        # Enviar el resultado como mensaje flash
        flash(f"Resultado de riesgo cardiovascular: {resultado['resultado']}")
        
        # Redirigir a la misma página para mostrar el resultado
        return redirect(url_for('cardio'))
    
    # Si es GET, mostrar el formulario
    return render_template('health_c_cardio.html')

@app.route('/cardio_graficos', methods=['GET'])
def cardio_graficos():
    return render_template('health_c_cardio_graphics.html')
    
@app.route('/cancermama')
def cancer_mama():
    return render_template('health_c_mama.html')

@app.route('/cancer_pulmon', methods=['GET', 'POST'])
def cancer_pulmon():
    if request.method == 'POST':
        genero = request.form.get('gender', 'Male')
        edad = int(request.form.get('age', 0))
        fumar = int(request.form.get('smoking', 0))
        dedos_amarillos = int(request.form.get('yellow_fingers', 0))
        ansiedad = int(request.form.get('anxiety', 0))
        presion_companeros = int(request.form.get('peer_pressure', 0))
        enfermedad_cronica = int(request.form.get('chronic_disease', 0))
        fatiga = int(request.form.get('fatigue', 0))
        alergia = int(request.form.get('allergy', 0))
        sibilancias = int(request.form.get('wheezing', 0)) 
        consumo_alcohol = int(request.form.get('alcohol_consuming', 0))
        tos = int(request.form.get('coughing', 0))
        dificultad_respirar = int(request.form.get('shortness_of_breath', 0))
        dificultad_tragar = int(request.form.get('swallowing_difficulty', 0))
        dolor_pecho = int(request.form.get('chest_pain', 0))

        # Llama a la función de predicción
        resultado = predecir_riesgo(genero, edad, fumar, dedos_amarillos, ansiedad, 
                                    presion_companeros, enfermedad_cronica, fatiga, 
                                    alergia, sibilancias, consumo_alcohol, tos, 
                                    dificultad_respirar, dificultad_tragar, dolor_pecho)

        flash(resultado["resultado"])
    
    return render_template('health_c_pulmon.html')


@app.route('/contacto')
def contacto():
    return render_template('contact.html')

@app.route('/cliente')
def cliente():
    return render_template('client.html')

@app.route('/noticias')
def noticias():
    return render_template('news.html')
    
if __name__ == '__main__':
    app.run(debug=True)