# CambioBot - Fintech Solutions

O CambioBot é um assistente virtual inteligente desenvolvido para otimizar a experiência de usuários em plataformas de fintech. Ele resolve o problema de perda de tempo com pesquisas manuais de taxas de câmbio, realizando conversões instantâneas via chat com dados em tempo real.

## Sobre o Projeto

Este projeto foi desenvolvido como parte do módulo de Chatbots, adaptando a lógica de consumo de APIs externas para o contexto financeiro. O bot identifica a intenção do usuário, extrai os valores e moedas, e consulta a cotação atualizada.

## Stack Técnica
#### Engine de NLP: Rasa Framework
#### Linguagem: Python 3.10+
#### Gerenciamento de Ambiente: Conda (Anaconda)
#### API de Dados: AwesomeAPI (Cotações em tempo real)
#### Arquitetura: Custom Actions (SDK Rasa) para processamento de lógica externa.

## Como Executar
1. Pré-requisitos
Certifique-se de ter o Conda instalado.

2. Configurando o Ambiente

cmd
#### Criar o ambiente
conda create --name cambiobot python=3.10

#### Ativar o ambiente
conda activate cambiobot

#### Instalar dependências
pip install rasa requests

3. Executando o Bot
Você precisará de dois terminais abertos:

Terminal 1 (Servidor de Actions):

cmd
rasa run actions

Terminal 2 (Interface do Bot):

cmd
rasa shell

#### Exemplo de Interação
Usuário: "Quanto vale 100 dólares em reais?"
CambioBot: "Cotação atual: 1 USD = 5.10 BRL. O valor de 100 USD equivale a R$ 510,00."

## Estrutura de Arquivos Principal
- actions/actions.py: Lógica de integração com a AwesomeAPI e cálculo de conversão.
- data/nlu.yml: Exemplos de frases para treinamento do modelo natural language.
- domain.yml: Definição de slots (valor, moeda_origem, moeda_destino) e respostas.
- environment.yml: Arquivo de exportação do ambiente Conda.

Desenvolvedor
Felipe Augusto
