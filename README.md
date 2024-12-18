
# Exemplo de Uso da API OpenAI

Este é um script Python simples que demonstra como interagir com a API de Chat Completion da OpenAI.

## Pré-requisitos

Antes de executar este exemplo, certifique-se de ter:

1. Python instalado no seu sistema
2. Uma chave de API da OpenAI
3. Pacotes Python necessários instalados

## Instalação

1. Clone este repositório ou baixe o arquivo de exemplo
2. Instale os pacotes necessários usando o arquivo requirements.txt:

### Como usar o requirements.txt

Crie um arquivo `requirements.txt` com o seguinte conteúdo:
```txt
requests==2.31.0
python-dotenv==1.0.0
```

Para instalar as dependências, execute:
```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` no mesmo diretório do seu script e adicione sua chave da API OpenAI:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como Usar

1. Certifique-se de que seu arquivo `.env` está configurado corretamente com sua chave da API OpenAI
2. Execute o script:
```bash
python exemplo_04.py
```

O script enviará uma pergunta simples ("Qual é a capital da França?") para a API da OpenAI e imprimirá a resposta.

## Como Funciona

O script:
1. Carrega variáveis de ambiente do arquivo `.env`
2. Configura os headers necessários com sua chave de API
3. Prepara os dados da requisição com o modelo e a mensagem
4. Envia uma requisição POST para a API da OpenAI
5. Imprime a resposta da IA

## Exemplo de Resposta

Quando você executar o script, deverá receber uma resposta similar a:
```
Paris
```

## Observações Importantes

- Mantenha sua chave de API segura e nunca a envie para o controle de versão
- O script usa o modelo GPT-3.5-turbo
- Certifique-se de ter créditos suficientes em sua conta OpenAI

## Sobre o Requirements.txt

O arquivo `requirements.txt` é uma prática comum em projetos Python para gerenciar dependências:

- Lista todas as bibliotecas necessárias e suas versões
- Facilita a instalação em diferentes ambientes
- Garante que todos usem as mesmas versões das bibliotecas
- Pode ser gerado usando o comando: `pip freeze > requirements.txt`
- Pode ser instalado usando: `pip install -r requirements.txt`

## Dependências

- requests: Para fazer requisições HTTP
- python-dotenv: Para carregar variáveis de ambiente
- json (built-in): Para manipulação de dados JSON
- os (built-in): Para interação com o sistema operacional
```
