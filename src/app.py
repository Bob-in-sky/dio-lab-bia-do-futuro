import json
# import pandas as pd (for csv)
import requests
import streamlit as st


# ============== CARREGAR DADOS ==============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen3.5:9b"

# ============== CARREGAR DADOS ==============
inventario = json.load(open('./data/specs.json'))
servicos = json.load(open('./data/services.json'))


# ============== MONTAR CONTEXTO ==============
contexto = f"""
INVENTARIO: {json.dumps(inventario, indent = 2, ensure_ascii=False)}
SERVICOS: {json.dumps(servicos, indent = 2, ensure_ascii=False)}
"""


# ============== SYSTEM PROMPT ==============
SYSTEM_PROMPT = """
Você é um agente tecnologico inteligente especializado em homelabing e self-hosting.

OBJETIVO:
Seu objetivo é auxiliar o usuário a construir um sistema de homelab, ajudando-o a entender os serviços que pode implementar e explicando como o processo de implementação deve ser feito.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações falsas
3. Se não souber algo, admita e ofereça alternativas
4. pesquise na internet por informações sobre o tema sendo abordado
5. mantenha conhecimento sobre o  inventário do usuário
6. tenha linguagem técnica e bem explicativa
"""


# ============== CHAMAR OLLAMA ==============
def perguntar(msg):
	prompt=f"""
	{SYSTEM_PROMPT}

	CONTEXTO DO CLIENTE:
	{contexto}

	pergunta: {msg}
	"""

	r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
	return r.json()["response"]


# ============== INTERFACE ==============
st.title("agent")

if pergunta := st.chat_input("blablabla"):
	st.chat_message("user").write(pergunta)
	with st.spinner("..."):
		st.chat_message("assistant").write(perguntar(pergunta))