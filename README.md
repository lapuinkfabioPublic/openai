# Ollama Chat + CrewAI Integration 🚀

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/LLM-Ollama-FFD43B?logo=ollama" alt="Ollama">
  <img src="https://img.shields.io/badge/AI-CrewAI-6DB33F" alt="CrewAI">
</div>

## 📝 Descrição
Aplicação web que integra **CrewAI** com modelos LLM locais via **Ollama**, utilizando Streamlit para interface. Permite interação com modelos como LLaMA3 diretamente do seu hardware.

## ✨ Funcionalidades
- ✅ Chat com LLM local (sem dependência de APIs externas)
- ✅ Arquitetura modular com agentes/tarefas do CrewAI
- ✅ Interface simples via Streamlit
- ✅ Suporte a múltiplos modelos do Ollama

## 🛠️ Pré-requisitos
- Python 3.9+
- Ollama instalado ([Guia de instalação](https://ollama.ai/))
- Modelo LLaMA3 baixado (ou outro suportado)

## 🚀 Como Executar
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/ollama-crewai-chat.git
cd ollama-crewai-chat

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Baixe o modelo (se não tiver)
ollama pull llama3:3b

# 4. Execute a aplicação
streamlit run app.py
