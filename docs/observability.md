# Observability

## Goal

Provide enough visibility to detect failures, understand system health, and support the final demo.

## Signals

- Application health.
- HTTP request volume and errors.
- Traefik access logs.
- PostgreSQL health.
- Host or container resource usage.
- Deployment status.

## Recommended Tools

- Prometheus for metrics.
- Grafana for dashboards.
- Loki or OpenSearch for logs.
- Alertmanager or cloud-native alerting for notifications.

## Open Decisions

- Self-managed or managed observability stack.
- Alert channels.
- Dashboard audience and required views.
