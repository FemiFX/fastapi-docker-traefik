# Architecture

## 1. Overview

The system is a small FastAPI service backed by PostgreSQL, exposed to the
outside world over HTTPS through Traefik. The application is intentionally
simple; the engineering value of the project is the **platform around it**:
multi-environment delivery, CI/CD, Infrastructure as Code, security,
data management, and observability.

The target runtime is a self-hosted **Proxmox VE** cluster. Staging and
production run on **k3s** (lightweight Kubernetes) clusters provisioned on
Proxmox VMs. Development stays on local Docker Compose for fast feedback.

## 2. Locked Decisions

These were open questions in the delivery plan and are now decided:

| Decision | Choice |
| --- | --- |
| SCM + CI/CD | GitHub (`FemiFX/fastapi-docker-traefik`) + GitHub Actions |
| Cloud / host | Self-hosted Proxmox VE |
| Production runtime | k3s (Kubernetes) on Proxmox VMs |
| Environments | Development (local Compose) + Staging (k3s) + Production (k3s) |
| IaC | Terraform (Proxmox provider) for VMs |
| Configuration as Code | Ansible + cloud-init for VM/k3s bootstrap |
| App deployment | Kubernetes manifests via Kustomize overlays (per environment) |
| Database | Self-hosted PostgreSQL in-cluster (StatefulSet + PVC) |
| Observability | kube-prometheus-stack (Prometheus + Grafana + Alertmanager) + Loki |

## 3. Current vs. Target

### Current (baseline in the repo)

- FastAPI service (`app/`) with a single `GET /` endpoint reading `User` rows.
- PostgreSQL via `databases` / `ormar` / SQLAlchemy.
- Traefik reverse proxy with HTTPS + Let's Encrypt + protected dashboard.
- Docker Compose for development (`docker-compose.yml`) and a Compose-based
  production path (`docker-compose.prod.yml`).
- Environment-variable-driven config; no hardcoded credentials.

### Target

- Local development on Docker Compose (unchanged).
- Staging and production on k3s, deployed automatically from GitHub Actions.
- HTTPS at the edge via Traefik (k3s ships Traefik as its default ingress).
- Persistent PostgreSQL with backup/restore.
- Centralized metrics, logs, dashboards, and alerts.
- All infrastructure and configuration reproducible from version control.

## 4. Logical Architecture

```
                          Internet (HTTPS)
                                |
                          [ Traefik Ingress ]   <- k3s built-in, TLS termination
                                |
                        [ FastAPI Deployment ]   <- 1..N replicas
                                |
                        [ PostgreSQL StatefulSet ]
                                |
                          [ PersistentVolume ]    <- Proxmox-backed storage

   Observability (in-cluster):
     Prometheus  <- scrapes app + Traefik + node + kube metrics
     Loki        <- aggregates container logs
     Grafana     <- dashboards (dev / ops / SRE views)
     Alertmanager<- routes alerts (downtime, error rate, cert expiry, disk)
```

## 5. Environment Topology

| Environment | Host | Runtime | Purpose |
| --- | --- | --- | --- |
| Development | Local workstation | Docker Compose | Fast inner-loop development |
| Staging | Proxmox VM(s) | k3s | Production-like validation before release |
| Production | Proxmox VM(s) | k3s | User-facing demo environment |

Staging and production are isolated at the VM and cluster level (separate
Proxmox VMs, separate k3s clusters or at minimum separate namespaces with
distinct credentials and DNS).

## 6. Components

| Component | Role | Current Status |
| --- | --- | --- |
| FastAPI | Application API | Present (needs `/health`, tests) |
| PostgreSQL | Persistent database | Present (needs in-cluster StatefulSet + backup) |
| Traefik | Reverse proxy / TLS / ingress | Present (Compose); to wire as k3s ingress |
| Docker Compose | Local dev orchestration | Present |
| k3s | Staging/prod orchestration | To build |
| Kustomize manifests | App deployment per environment | To build |
| Terraform (Proxmox) | VM provisioning (IaC) | To build |
| Ansible / cloud-init | VM + k3s configuration (CaC) | To build |
| GitHub Actions | Lint, test, build, scan, deploy (PaC) | To build |
| kube-prometheus-stack + Loki | Observability | To build |

## 7. Request & Deployment Flows

**Request flow (staging/prod):** client → DNS → Proxmox VM public IP →
Traefik ingress (TLS) → FastAPI service → PostgreSQL.

**Deployment flow:** push/PR → GitHub Actions (lint → test → build image →
scan → push to registry) → deploy to staging (Kustomize apply) → smoke tests →
manual approval → deploy to production.

## 8. Diagrams To Produce

- Component diagram (app, db, proxy, observability) — for the submission.
- Network/infrastructure diagram (Proxmox host, VMs, k3s, DNS, firewall).
- CI/CD pipeline diagram (stages and environment promotion).
- Deployment sequence (commit → production).
