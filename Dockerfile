# ---------- build ----------
FROM python:3.12 AS base

FROM base AS builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONUTF8=1 \
    PATH="$PATH:/runtime/bin" \
    PYTHONPATH="/runtime/lib/python3.12/site-packages"

WORKDIR /opt

COPY requirements.lock ./
RUN pip install --prefix=/runtime --force-reinstall -r requirements.lock

# ---------- runtime ----------
FROM python:3.12-slim as runtime

RUN groupadd -g 999 app && \
    useradd -d /app -s /bin/bash -u 999 -g 999 app
COPY --from=builder /runtime /usr/local

WORKDIR /app/admin

copy manage.py ./
copy admin ./admin

USER app

CMD exec gunicorn admin.wsgi:application -w 1 --threads 8 --bind 0.0.0.0:8000 --max-requests 10000 --timeout 180 --graceful-timeout 180
