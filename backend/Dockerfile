FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8000
CMD ["./entrypoint.sh"]
