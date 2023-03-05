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

# Passos

1. Instale o pytest na build da aplicação
2. Configure o mínimo do pytest para conseguir rodar um teste unitário
3. Implemente uma forma de rodar os testes:
   - comando básico para rodar pelo docker
   - pre-commit
   - ci/cd pipeline
4. Implemente um teste unitário para a lógica X da aplicação
5. Configure o pytest para conseguir rodar testes que dependem de banco
6. Implemente um teste que depende de banco
7. Implemente um teste das tasks do celery
8. Implemente um teste parametrizado
9. Implemente um report da métrica de cobertura de testes

# TODOs

- [x] Rota de predict
- [x] Resources com os modelos e arquivos do pipeline
- [ ] Salvar a predição no banco
- [ ] Enviar um link de uma nova para base para retreino
- [ ] Retreino salvar no banco o processamento e atualizar para processado
- [ ] Atualizar rota que busca pelo status do treinamento
- [ ] Adicionar um schema de output, para ter insumo para criar teste
