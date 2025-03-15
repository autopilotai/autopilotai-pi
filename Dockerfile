FROM cgr.dev/chainguard/python:latest-dev as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/app/venv/bin:$PATH"

USER root
RUN apk update && apk add \
    libgomp

WORKDIR /app

RUN python -m venv venv
COPY app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]