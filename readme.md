# Lex Simplifica IA - Projeto Imersão IA Alura + Google

Este projeto é um agente de IA que simplifica textos jurídicos complexos utilizando a API Google Gemini. 
O objetivo é tornar a linguagem jurídica mais acessível para pessoas leigas.

## Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone URL_DO_SEU_REPOSITORIO
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua API Key:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua Google API Key ao arquivo `.env` da seguinte forma:
        ```
        GOOGLE_API_KEY="SUA_API_KEY_AQUI"
        ```
    * **Este arquivo não deve ser enviado para o GitHub.**

5.  **Execute o aplicativo Flask:**
    ```bash
    python app.py
    ```

6.  Abra seu navegador e acesse `http://127.0.0.1:5000/`.

## Tecnologias Utilizadas
* Python
* Flask
* Google Gemini API (via `google-generativeai`)
* HTML, CSS, JavaScript