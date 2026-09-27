# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `specs.json` | JSON | Inventário do usuário |
| `services.json` | JSON | Servicos implementados no homelab do usuario |

<!-- > [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio. -->

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados para contextualizar o agente com informações relevantes ao processo de homelabing

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt, e serão armazenados para serem utilizados no contexto global do agente, que deve estar ciente de como o ambiente do usuario está catalogado no momento

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados podem ser consultados e alterados dinamicamente conforme o usuario implementa seus projetos no sistema, quando necessario o agente deve buscar informações na internet para poder tirar as duvidas do usuario quanto às tecnologias que deseja implementar

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

o exemplo de contecto abaixo se baseia nos dados originais da base de conhecimento, resumidos para otimizar o consumo de tokenns, porém a prioridade do agente se encontra em ter as informações disponiveis sobre o sistema que o usuario esta montando, para que o usuario possa consultar e tirar duidas sem que apresente seu sistema toda hora.

```
Inventário do usuário:
- desktop: 1
	- cpu: R7 5700X3D
	- gpu: 4060TI 8GB
	- ram: 16GB
	- ssd: 1TB
	- hdd: 1TB
- laptop: 1
	- cpu: intel core i7
	- gpu: intel iris xe
	- ram: 8GB
- raspberry pi 5: 1
	- ram: 8GB
	- hdd: 500GB
	- sd card: 8GB

servicos implementados:
- jellyfin server
- pi-hole
- portainer
- docker
- tailscale
- file browser
...
```
