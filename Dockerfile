FROM python:3.11-slim

# Installazione librerie di sistema
RUN apt-get update && apt-get install -y \
    libhidapi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia dei file nel container
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Porta che esporrà l'app web
EXPOSE 80

# Comando per avviare l'app
CMD ["python", "app.py"]