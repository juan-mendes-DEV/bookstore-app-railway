import os
from pathlib import Path
from urllib.parse import urlparse
import dj_database_url  # Para parsear a URL do banco de dados

BASE_DIR = Path(__file__).resolve().parent.parent

# Alterar para False em produção
DEBUG = True  # Altere para False em produção

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework.authtoken",
    "rest_framework",
    "django_extensions",
    "debug_toolbar",
    "order",
    "product",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Para servir arquivos estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Ativado em DEBUG
]

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"

# Banco de dados PostgreSQL
# Usa a variável DATABASE_URL, mas mantém as variáveis de configuração explícitas

DATABASE_URL = os.getenv("DATABASE_URL")  # Usará a URL do banco de dados, se fornecida

if DATABASE_URL:
    # Se a variável DATABASE_URL estiver configurada, usa ela
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,  # Aqui busca pela variável de ambiente DATABASE_URL
            conn_max_age=600,  # Aumenta o tempo de vida da conexão (opcional)
        )
    }
else:
    # Caso contrário, usa as variáveis tradicionais do banco de dados
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("SQL_DATABASE", "bookstore_db"),
            "USER": os.environ.get("SQL_USER", "postgres"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "PtyCUJaEoPBnxrcNeHHuxjFjUufIQILk"),
            "HOST": os.environ.get("SQL_HOST", "postgres.railway.internal"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
        }
    }

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # Diretório para arquivos coletados

# WhiteNoise para servir arquivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

INTERNAL_IPS = [
    "127.0.0.1",
]

# SECRET_KEY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default_secret_key_for_testing')  # Coloque uma chave segura temporariamente

# ALLOWED_HOSTS (Comente temporariamente as restrições)
ALLOWED_HOSTS = ["*"]  # Aceitar qualquer host por enquanto, apenas para testes

# Segurança - Desative essas configurações para testes
CSRF_COOKIE_SECURE = False  # Desative para testes
SESSION_COOKIE_SECURE = False  # Desative para testes
SECURE_SSL_REDIRECT = False  # Desative para testes
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 0  # Desative para testes
SECURE_HSTS_INCLUDE_SUBDOMAINS = False  # Desative para testes
SECURE_HSTS_PRELOAD = False  # Desative para testes


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# export DATABASE_URL="postgres://user:password@postgres.railway.internal:5432/bookstore_db"
# export DJANGO_SECRET_KEY="your_secret_key_here"