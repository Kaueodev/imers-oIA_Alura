import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import fitz  # PyMuPDF

load_dotenv()

app = Flask(__name__)

try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("API Key não encontrada. Verifique seu arquivo .env")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Erro ao configurar a API Key: {e}")

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

@app.route('/extrair_texto_pdf', methods=['POST'])
def extrair_texto_do_pdf():
    if 'pdf_file' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return jsonify({'erro': 'Nome de arquivo vazio'}), 400

    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return jsonify({'texto': text})

    except Exception as e:
        return jsonify({'erro': 'Erro ao extrair texto do PDF', 'detalhes': str(e)}), 500

@app.route('/simplificar', methods=['POST'])
def simplificar_texto():
    if not request.is_json:
        data = request.form  # Tenta ler do formulário (upload de arquivo)
        if not data:
            return jsonify({"erro": "Request deve ser JSON ou form-data"}), 400
        texto_juridico = data.get('texto')
    else:
        data = request.get_json()
        texto_juridico = data.get('texto')

    if not texto_juridico:
        return jsonify({"erro": "Nenhum texto fornecido"}), 400
    
    print('Texo jurídico recebido:', texto_juridico)

    try:
        prompt_parts = [
            "Você é um especialista em análise e simplificação de textos jurídicos complexos. Sua missão é ler cuidadosamente documentos legais e transformá-los em uma linguagem clara, acessível e direta, como se você estivesse explicando a um amigo ou familiar sem conhecimento prévio em direito. Mantenha um tom sério e objetivo, garantindo a precisão das informações, mas evite jargões técnicos desnecessários e construções frasais rebuscadas. Ao apresentar a versão simplificada, destaque de forma explícita e inequívoca os pontos MAIS IMPORTANTES do texto original. Utilize recursos como frases curtas, exemplos práticos (se aplicável) e formatação (como negrito ou marcadores) para enfatizar esses pontos cruciais e garantir que qualquer pessoa possa compreender a essência do documento e suas implicações. Importante: Ao final da sua análise e simplificação, inclua a seguinte mensagem para o usuário: 'Esta é uma versão simplificada para facilitar a compreensão. Para informações precisas e aconselhamento legal, consulte sempre um profissional da área jurídica.",
            "Texto jurídico para análise:",
            texto_juridico,
            "Sua explicação simplificada:"
        ]

        print("Enviando prompt para o Gemini...")
        response = model.generate_content(prompt_parts)
        print("Resposta recebida do Gemini.")

        texto_simplificado = response.text
        return jsonify({"texto_simplificado": texto_simplificado})

    except Exception as e:
        print(f"Erro ao chamar a API do Gemini: {e}")
        return jsonify({"erro": "Erro ao processar o texto com a IA", "detalhes": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)