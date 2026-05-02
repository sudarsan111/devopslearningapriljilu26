# Stage 1 — install dependencies
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2 — lean runtime image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY src/ ./src/
ENV FLASK_APP=src.app:create_app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
