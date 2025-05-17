import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

app = Flask(__name__)

# Configuração da API Key do Google
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API Key não encontrada. Verifique seu arquivo .env")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Erro ao configurar a API Key: {e}")

# Configuração do modelo Gemini
generation_config = {
    "temperature": 0.7, 
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048, 
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash", 
    generation_config=generation_config,
    safety_settings=safety_settings
)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/simplificar', methods=['POST'])
def simplificar_texto():
    if not request.is_json:
        return jsonify({"erro": "Request deve ser JSON"}), 400

    data = request.get_json()
    texto_juridico = data.get('texto')

    if not texto_juridico:
        return jsonify({"erro": "Nenhum texto fornecido"}), 400

    try:
        
        prompt_parts = [
            "Você é um assistente especialista em traduzir linguagem jurídica complexa para uma linguagem simples e clara, como se estivesse explicando para uma pessoa leiga.",
            "Analise o seguinte texto jurídico e reescreva-o de forma didática, explicando os pontos principais, direitos, deveres e quaisquer termos complexos.",
            "Texto jurídico para análise:",
            texto_juridico,
            "Sua explicação simplificada:"
        ]

        print("Enviando prompt para o Gemini...") # Log para debug
        response = model.generate_content(prompt_parts)
        print("Resposta recebida do Gemini.") # Log para debug

        texto_simplificado = response.text
        return jsonify({"texto_simplificado": texto_simplificado})

    except Exception as e:
        print(f"Erro ao chamar a API do Gemini: {e}") # Log para debug
        return jsonify({"erro": "Erro ao processar o texto com a IA", "detalhes": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 