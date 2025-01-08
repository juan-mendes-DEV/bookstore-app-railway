# Base image com Python 3.12.1
FROM python:3.12.1-slim AS python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona o diretório do poetry e do venv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update -y && apt-get install --no-install-recommends -y \
    curl build-essential libpq-dev gcc python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Instala o Poetry usando pip
RUN pip install poetry

# Instala dependências do Postgres
RUN apt-get update -y && apt-get install -y libpq-dev gcc && \
    pip install psycopg2

# Copia os arquivos de configuração do Poetry
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instala as dependências do projeto
RUN poetry install --only main --no-root

# Define o diretório de trabalho da aplicação
WORKDIR /app

# Copia o projeto para o container
COPY . /app/

# Exporta a porta 8000
EXPOSE 8000

# Comando para executar o servidor
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:8000"]