# 💥 Dojo Testes

A ideia desse Dojo é conseguir trazer um aprendizado sobre a utilização de testes unitários em uma API.

O contexto onde os testes serão configurados gira em torno do seguinte case:

> Uma API que serve um modelo de machine learning de previsão de fraude, e com base em um determinado input, o modelo te retorna se a transação foi fraude ou não.

Essa API possui os seguintes componentes:

- FastAPI
- Celery para tasks que rodam em background
- Banco de dados para armazenar informação das predições
- Docker para conteneirizar a aplicação
- Pytest para implementação dos testes

# Como Reproduzir o ambiente?

(WIP)

# O que vamos testar?

- Formatação de Input e Output da API
- Testes da Lógica da API
- Testes de Interação com o banco da aplicação
- Testes do modelo
- Testes do celery

# Conceitos importantes a se aprender do Pytest

- Instalação
- Configuração
- Como Funciona?
- Escrevendo um teste...
- Parametrizando um teste...
