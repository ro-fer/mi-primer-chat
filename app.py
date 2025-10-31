from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Respuestas preprogramadas para empezar
respuestas = {
    "hola": "¡Hola! Soy tu asistente biomédico. ¿En qué puedo ayudarte?",
    "como estas": "¡Estoy bien! Listo para ayudarte con tus consultas.",
    "que puedes hacer": "Puedo responder preguntas básicas sobre documentación biomédica.",
    "default": "Interesante pregunta. Por ahora soy un prototipo básico, pero pronto aprenderé más!"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message'].lower()
        
        # Buscar respuesta
        for key in respuestas:
            if key in user_message:
                return jsonify({'response': respuestas[key]})
        
        return jsonify({'response': respuestas['default']})
        
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)