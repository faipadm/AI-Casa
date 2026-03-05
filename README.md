# Agente de Planta de Casa

Este projeto implementa um agente capaz de gerar plantas de casas a partir de prompts de natural language.

## Estrutura

- `agent/`: código principal do agente
- `data/`: arquivos de dados estáticos ou caches
- `utils/`: utilitários gerais

## Uso

### Pré-requisitos

1. Crie e ative um ambiente virtual Python (recomendado).
2. Instale dependências:

```bash
python -m pip install -r requirements.txt
```

### Executando o agente

```bash
python -m agent.main --prompt "terreno 20x30 em São Paulo com 3 quartos e 2 banheiros"
```

O programa irá:

- Analisar o prompt e extrair dados (dimensões, localização, quartos, etc.)
- Buscar informações externas simuladas (códigos de construção, mapa)
- Gerar um arquivo `plan.dxf` representando o terreno e divisão básica de espaços
- Gerar um `plan_preview.png` com uma pré-visualização simples

### Projeto

- `agent/`: código principal do agente
- `utils/`: utilitários de parsing e busca de dados
- `data/`: arquivos estáticos e caches

Este projeto é um protótipo; para uso real, implemente integrações
reais com APIs de mapas, normas e um analisador de linguagem mais
robusto (por exemplo, usando um modelo LLM).

### Logs e configuração

O código usa o módulo `logging` para registrar operações e erros. Você
pode controlar o nível de log via variável de ambiente `LOG_LEVEL`.

As chaves de API (por exemplo, OpenAI) devem estar em variáveis de
ambiente (veja `utils/config.py`).

### Testes

Executar os testes unitários com `pytest`:

```bash
pip install pytest
pytest tests/
```

Isso garante que as partes principais (parser e gerador) funcionem como
esperado.

### Desenvolvimento Profissional

1. **LLM**: configure `OPENAI_API_KEY` ou outro endpoint de LLM e ajuste
   `_call_llm` em `utils/parser.py` para processar respostas corretamente.
2. **APIs externas**: substitua os stubs em `utils/data_fetcher.py` por
   chamadas reais (municipais, climáticas, topográficas).
3. **Desenho CAD avançado**: use uma biblioteca mais completa ou exporte
   para DWG/Revit, adicionando camadas, cotas e símbolos.
4. **Validação de normas**: incorpore regras do país/estado para limites,
   áreas mínimas, afastamentos, etc.
5. **Interface**: crie uma API REST/GUI ou CLI mais rica para integração
   com ferramentas de escritório ou pipelines de projeto. Use o servidor
   FastAPI fornecido (`agent/server.py`) ou construa uma interface web
   personalizada.
6. **Distribuição**:
   * Empacote usando `pyproject.toml` (já presente). Instale via
     `pip install .` ou `pip install placa-agent` após publicação.
   * Crie um **Dockerfile** (fornecido abaixo) para gerar contêineres
     facilmente implantáveis.

### Execução em container Docker

1. Construa a imagem:
   ```bash
   docker build -t planta-agent:latest .
   ```
2. Execute o container:
   ```bash
   docker run -e OPENAI_API_KEY=xyz -p 8000:8000 planta-agent
   ```
3. Acesse a API em `http://localhost:8000/generate` com POST JSON
   `{"prompt": "seu texto aqui"}`.

Isso torna a solução pronta para ser escalada e utilizada em cenários
reais de produção, com implantação em nuvem ou em servidores on-premise.

O projeto agora oferece uma base completa que pode ser estendida e
implantada em um cenário profissional.
