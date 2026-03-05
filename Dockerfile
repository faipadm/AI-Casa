# Dockerfile para agente de planta de casa
FROM python:3.11-slim

# definir diretório de trabalho
WORKDIR /app

# copiar arquivos de requerimentos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar todo o código
COPY . /app

# expor porta para API
EXPOSE 8000

# variáveis de ambiente default (podem ser substituídas)
ENV LOG_LEVEL=INFO

# comando padrão: inicia servidor uvicorn
CMD ["uvicorn", "agent.server:app", "--host", "0.0.0.0", "--port", "8000"]
