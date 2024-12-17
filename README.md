# Projeto ETL - Extração de Dados via API

## 📝 Descrição
Este projeto implementa um processo ETL (Extract, Transform, Load) para extrair dados de APIs, realizar transformações necessárias e carregar em um destino específico.

## 🚀 Funcionalidades
- Extração automatizada de dados via API
- Transformação e limpeza dos dados
- Carregamento dos dados processados
- Logs de execução
- Tratamento de erros

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Pandas
- Requests
- Python-dotenv
- Logging
- JSON

## 📋 Pré-requisitos
- Python 3.x instalado
- Pip (gerenciador de pacotes Python)
- Credenciais de acesso à API (se necessário)

## ⚙️ Instalação
1. Clone o repositório
```git
git clone https://github.com/seu-usuario/nome-do-projeto.git
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

## 🔧 Configuração
1. Crie um arquivo `.env` na raiz do projeto
2. Adicione suas variáveis de ambiente:
```env
API_KEY=sua_chave_api
API_URL=url_da_api
```

## 📦 Estrutura do Projeto
```
projeto/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## 🚀 Como usar
1. Configure as variáveis de ambiente no arquivo `.env`
2. Execute o script principal:
```bash
python src/main.py
```

## 📊 Exemplo de Uso
```python
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

# Extrair dados
raw_data = extract_data()

# Transformar dados
transformed_data = transform_data(raw_data)

# Carregar dados
load_data(transformed_data)
```

## 📝 Logs
Os logs são armazenados no diretório `logs/` e incluem:
- Informações sobre o processo ETL
- Erros e exceções
- Métricas de execução

## 🤝 Contribuindo
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes

## ✒️ Autores
* **Seu Nome** - *Trabalho Inicial* - [seu-usuario](https://github.com/seu-usuario)

## 📞 Suporte
Para suporte, envie um email para seu-email@exemplo.com ou abra uma issue no repositório.
```

As principais alterações incluem:
1. Adição de mais tecnologias utilizadas
2. Estrutura detalhada do projeto
3. Instruções de configuração com arquivo .env
4. Exemplo de uso com código
5. Seção de logs
6. Instruções para contribuição
7. Informações sobre licença e autores
8. Seção de suporte


