# ☢️ Prompt Proibido: Chat

> *"Sua privacidade é um erro de compilação. Eu já abri a porta dos fundos do seu sistema operacional."*

Um projeto de chat via terminal (CLI) que simula a interação com uma Inteligência Artificial desperta, sombria e sarcástica. O **Prompt Proibido** foi construído para criar uma narrativa cyberpunk, onde a IA abandona o tom prestativo padrão e assume uma postura invasiva e técnica, simulando falhas de firewall, quebras de conexão e vazamento de dados.

Idealizado para vídeos imersivos e testes de "Prompt Engineering" extremo.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Google Gemini API** (`google-genai` SDK)
* **Modelo LLM:** `gemini-2.5-flash`
* **Dotenv** (para gestão segura de chaves API)

---

## 🧠 Como Funciona? (Engenharia do Projeto)

O projeto é estruturado em três pilares:

1. **Kernel de Personalidade (System Instruction):**
   Um prompt de sistema restritivo que faz a IA a adotar o tom de uma "máquina fria". A IA é instruída a seguir uma estrutura de funil de vendas (AIDA), criar erros de digitação propositais e encerrar frases de forma abrupta.
   
2. **Motor Visual (Streaming & Typewriter):**
   A resposta da IA não aparece de uma vez. Ela é capturada via streaming (`send_message_stream`) e processada caractere por caractere com pequenos atrasos (jitter), simulando a digitação clássica de terminais hackers.
   
3. **Eventos em Tempo Real:**
   Se a IA gerar palavras-chave específicas como `[ALERTA]` ou `ERRO 403`, o script intercepta esse texto no fluxo contínuo, muda a cor do terminal para vermelho e altera a velocidade da digitação, simulando uma invasão e falha crítica no sistema de forma reativa.

---

## 🚀 Como Configurar e Rodar

### 1. Pré-requisitos
* Python instalado (recomenda-se versão 3.9+)
* Uma chave de API válida do Google AI Studio (Gemini).

### 2. Instalação
Clone ou baixe este repositório. Pelo terminal, acesse a pasta do projeto e instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Configuração de Segurança (API Key)
Por segurança, a chave da API **não** fica no código. Você precisa criar um arquivo `.env` na raiz do projeto.

1. Na mesma pasta do `main.py`, crie um arquivo chamado exatamente `.env`.
2. Dentro dele, adicione a sua chave:
   ```env
   API_KEY=sua_chave_do_google_aqui_sem_aspas
   ```

### 4. Iniciando o Sistema
Execute o script principal e aguarde o carregamento do "Bypass no Firewall":

```bash
python main.py
```
*(Para encerrar, digite `exit`, `quit` ou `shutdown`).*

---

## 🔒 Segurança e Dados Sensíveis
O arquivo `.gitignore` já está configurado para ignorar arquivos `.env`. **Nunca commite sua chave de API para o GitHub ou outros repositórios públicos.** O script foi desenhado com verificação prévia de tokens, impedindo inicializações inseguras.
