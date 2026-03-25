# CambioBot - Fintech Solutions

O **CambioBot** é um assistente virtual inteligente desenvolvido para otimizar a experiência de usuários em plataformas de fintech. Ele resolve o problema de perda de tempo com pesquisas manuais de taxas de câmbio, realizando conversões instantâneas via chat com dados em tempo real.


## Sobre o Projeto

Este projeto foi desenvolvido como parte do módulo de **Chatbots**, adaptando a lógica de consumo de APIs externas para o contexto financeiro. O bot utiliza Processamento de Linguagem Natural (NLP) para identificar a intenção do usuário, extrair valores e moedas, e consultar a cotação atualizada.


## Stack Técnica

* **NLP Engine:** Rasa Framework 3.x
* **Linguagem:** Python 3.10+
* **Gerenciamento de Ambiente:** Conda (Anaconda)
* **API de Dados:** [AwesomeAPI](https://docs.awesomeapi.com.br/) (Cotações em tempo real)
* **Arquitetura:** Custom Actions (SDK Rasa) para processamento de lógica externa.


## Como Executar

### 1. Configurando o Ambiente
No terminal, utilize o Conda para isolar as dependências e evitar conflitos:

    ```bash
    # Criar o ambiente
    conda create --name cambiobot python=3.10 -y
    
    ```bash
    # Ativar o ambiente
    conda activate cambiobot
    
    ```bash
    # Instalar dependências
    pip install rasa requests


### 2. Executando a Aplicação
Você precisará de dois terminais abertos simultaneamente:

Terminal 1 (Servidor de Actions):

    ```bash
    rasa run actions
    
Terminal 2 (Interface do Bot):

    ```bash
    rasa train
    rasa shell
    
#### Exemplo de Interação

Usuário: "Quanto vale 100 dólares em reais?"

CambioBot: "Cotação atual: 1 USD = 5.10 BRL. O valor de 100 USD equivale a R$ 510,00."


## Estrutura de Arquivos

- actions/actions.py → Integração com AwesomeAPI e cálculos de conversão
- data/nlu.yml → Exemplos de treinamento (intents e entities)
- domain.yml → Configuração de slots e respostas do bot
- environment.yml → Replicação do ambiente de desenvolvimento


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Rasa](https://img.shields.io/badge/rasa-5A17EE?style=for-the-badge&logo=rasa&logoColor=white)
![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)


Desenvolvedor: Felipe Augusto da Silva
