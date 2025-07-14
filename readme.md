# LexIA: Simplificando o Juridiquês com Inteligência Artificial

LexIA é uma aplicação web desenvolvida para traduzir textos jurídicos complexos em uma linguagem clara, simples e acessível para todos. Utilizando o poder do Google Gemini, a ferramenta analisa documentos legais e os reescreve de forma que qualquer pessoa, independentemente de seu conhecimento em direito, possa compreender seus direitos, deveres e as implicações do texto.

Este projeto foi desenvolvido como parte da **Imersão IA**, uma iniciativa da **Alura** em parceria com o **Google**.

## O que o projeto faz?

- **Simplificação de Textos:** Cole um trecho de um contrato, lei ou qualquer documento jurídico e receba uma versão simplificada em segundos.
- **Extração de PDF:** Faça o upload de um arquivo PDF e a ferramenta extrairá automaticamente o texto para simplificação.
- **Acessibilidade:** Torna o jargão jurídico compreensível para estudantes, profissionais de outras áreas e o público em geral.

## Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

- **Backend:** Python, Flask
- **Inteligência Artificial:** Google Gemini
- **Manipulação de PDF:** PyMuPDF (fitz)
- **Frontend:** HTML, CSS, JavaScript
- **Gerenciamento de Variáveis de Ambiente:** python-dotenv

## Como Executar o Projeto Localmente

Para rodar a aplicação em seu ambiente de desenvolvimento, siga os passos abaixo.

### Pré-requisitos

- Python 3.x
- Uma chave de API do Google Gemini. Você pode obter uma no [Google AI Studio](https://aistudio.google.com/app/apikey).

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/lexia.git
    cd lexia
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    - No Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**

    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Adicione sua chave de API do Google ao arquivo:
      ```
      GOOGLE_API_KEY=SUA_CHAVE_DE_API_AQUI
      ```

5.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

6.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://12.0.0.1:5000`.

## Como Usar

1.  **Opção 1: Colar Texto:** Cole o texto jurídico diretamente na área de texto designada.
2.  **Opção 2: Upload de PDF:** Clique no botão de upload e selecione um arquivo PDF do seu computador. O texto será extraído automaticamente.
3.  **Simplificar:** Clique no botão "Simplificar" e aguarde a IA processar e retornar a versão simplificada do texto.

## Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma ideia para melhorar o projeto, encontrou um bug ou quer adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

Feito com ❤️ para a Imersão IA da Alura + Google.
