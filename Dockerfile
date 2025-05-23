# Utiliser une image Python officielle comme image de base
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./datasets /app/datasets
COPY . .

EXPOSE 8000

CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000"]
