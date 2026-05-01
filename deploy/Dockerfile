FROM caddy:2-alpine AS caddy-bin

FROM python:3.12-slim

# Install Caddy and rsync
COPY --from=caddy-bin /usr/bin/caddy /usr/bin/caddy
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    rsync \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Webhook receiver
WORKDIR /opt/webhook
COPY webhook-receiver.py .
COPY deploy.sh .
RUN chmod +x deploy.sh

# Caddy config
COPY Caddyfile /etc/caddy/Caddyfile

# Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/services.conf

# Site content volume
RUN mkdir -p /srv/csrameshcore
VOLUME /srv/csrameshcore

EXPOSE 80 443

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
