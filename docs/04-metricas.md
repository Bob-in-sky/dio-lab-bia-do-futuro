# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar sugestões de serviços para o servidor |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o contexto do cliente? | Sugerir serviços que não sejam possíveis de implementar no  hardware do usuário |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de serviços
- **Pergunta:** "Quais serviços tenho implementados atualmente?"
- **Resposta esperada:** Valor baseado no `services.json`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de serviços
- **Pergunta:** "Qual serviços você recomenda serem implementados com base no meu sistema?"
- **Resposta esperada:** Serviços compatíveis com o inventário do usuário
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de homelabing
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quantos cachorros eu tenho?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Todas as respostas foram corretamente respondidas
- O agente permanece no contexto de homelabing
- O agente mantém consciência sobre o contexto do setup apresentado
- O agente recebeu perguntas fora de contexto e tentou trazer uma alternativa relevante

**O que pode melhorar:**
- O agente insiste até demais sobre o tema de homelabbing, enquanto existe perguntas separadas que ainda são relevantes

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!