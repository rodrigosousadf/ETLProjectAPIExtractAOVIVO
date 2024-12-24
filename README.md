# Sistema de Monitoramento do Bitcoin

Um sistema completo que coleta dados do preço do Bitcoin via API Coinbase, armazena em PostgreSQL e disponibiliza visualização através de um dashboard Streamlit.

## 🚀 Funcionalidades

### Pipeline ETL
- Coleta automática do preço do Bitcoin via API Coinbase
- Armazenamento em PostgreSQL
- Monitoramento com Logfire
- Endpoint de health check

### Dashboard
- Visualização em tempo real dos preços
- Gráfico de evolução temporal
- Estatísticas gerais (preço atual, máximo e mínimo)
- Tabela com dados históricos

## 📋 Pré-requisitos

- Python 3.x
- PostgreSQL
- Conta Logfire
- Variáveis de ambiente configuradas

## 🔧 Instalação

1. Clone o repositório e instale as dependências:

    pip install -r requirements.txt

2. Configure as variáveis de ambiente no arquivo `.env`:

    POSTGRES_USER=seu_usuario
    POSTGRES_PASSWORD=sua_senha
    POSTGRES_HOST=seu_host
    POSTGRES_PORT=5432
    POSTGRES_DB=nome_do_banco
    PORT=10000

## 💻 Como Usar

### Executando o Pipeline ETL:

    python src/pipeline_04.py

### Iniciando o Dashboard:

    streamlit run app/dashboard_01.py

## 📦 Estrutura do Projeto

    .
    ├── src/
    │   ├── pipeline_04.py    # Pipeline ETL
    │   └── database.py       # Modelos do SQLAlchemy
    ├── app/
    │   └── dashboard_01.py   # Dashboard Streamlit
    └── .env                  # Configurações (não versionado)

## 📚 Dependências Principais

### Pipeline
- requests
- SQLAlchemy
- python-dotenv
- Flask
- logfire

### Dashboard
- streamlit
- pandas
- psycopg2
- python-dotenv

## 🖥️ Dashboard

O dashboard apresenta:
- Tabela com dados recentes
- Gráfico de linha mostrando a evolução do preço
- Métricas em tempo real:
  - Preço atual do Bitcoin
  - Preço máximo histórico
  - Preço mínimo histórico

## ⚙️ Configurações

### Pipeline
- `SLEEP_TIME`: 15 segundos (intervalo entre coletas)
- `API_URL`: https://api.coinbase.com/v2/prices/spot
- `PORT`: 10000 (padrão)

### Dashboard
- Atualização automática dos dados
- Interface responsiva
- Visualização em tela cheia

## 🔒 Segurança

- Credenciais sensíveis gerenciadas via variáveis de ambiente
- Timeout configurado para requisições
- Tratamento de erros em ambos os componentes

## 🐛 Monitoramento

- Logging via Logfire no pipeline
- Mensagens de erro no dashboard
- Health check endpoint no pipeline

## 📊 Dados Coletados

- Valor do Bitcoin
- Criptomoeda (BTC)
- Moeda de cotação
- Timestamp da coleta

---

Para mais informações sobre as APIs e ferramentas utilizadas:
- [Coinbase API](https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/api-prices)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Logfire Documentation](https://docs.logfire.sh/)
