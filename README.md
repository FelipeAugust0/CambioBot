# CambioBot - Fintech Solutions

O **CambioBot** é um assistente virtual inteligente projetado para otimizar a experiência de usuários em plataformas de fintech. Ele elimina a necessidade de pesquisas manuais de taxas de câmbio, realizando conversões instantâneas via chat com dados em tempo real.


## Sobre o Projeto
Desenvolvido como parte do módulo de Chatbots (baseado no conceito de integração de APIs externas), o bot utiliza **NLP** (Processamento de Linguagem Natural) para identificar intenções, extrair entidades (valores e moedas) e consultar cotações atualizadas.


## Stack Técnica
* **NLP Engine:** Rasa Framework 3.x
* **Linguagem:** Python 3.10+
* **Ambiente:** Conda (Anaconda)
* **API:** [AwesomeAPI](https://docs.awesomeapi.com.br/) (Cotações em tempo real)
* **Arquitetura:** Custom Actions (SDK Rasa)


## Como Executar?

### 1. Configurando o Ambiente
No terminal, utilize o Conda para isolar as dependências e evitar conflitos:

###### Criar e ativar o ambiente
conda create --name cambiobot python=3.10 -y
conda activate cambiobot

###### Instalar dependências
pip install rasa requests


### 2. Rodando a Aplicação
Você precisará de dois terminais abertos simultaneamente:

Terminal 1:
rasa run actions

Terminal 2:
rasa train
rasa shell


###### Exemplo de Interação
Usuário: "Quanto vale 100 dólares em reais?"
CambioBot: "Cotação atual: 1 USD = 5.10 BRL. O valor de 100 USD equivale a R$ 510,00."


###### Estrutura de Arquivos
- actions/actions.py: Integração com AwesomeAPI e cálculos de conversão.
- data/nlu.yml: Exemplos de treinamento para reconhecimento de frases (Intents/Entities).
- domain.yml: Configuração de slots (memória do bot) e respostas do sistema.
- environment.yml: Arquivo para replicação exata do ambiente de desenvolvimento.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Rasa](https://img.shields.io/badge/rasa-5A17EE?style=for-the-badge&logo=rasa&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)

Desenvolvedor: Felipe Augusto da Silva
