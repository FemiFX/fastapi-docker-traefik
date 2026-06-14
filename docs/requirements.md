# Requirements

## Purpose

Define the functional and non-functional requirements that guide architecture,
implementation, deployment, and defense decisions. This document is the grid
against which design choices are justified.

## Context

DevOps & Cloud Architecture training project (DataScientest "DevOps
Administrator" title). A deliberately simple FastAPI + PostgreSQL application
is the vehicle for demonstrating a full DevOps platform. Assessment is by jury
defense in Week 6 (20-min presentation + demo, 10-min questions). The target
host is a self-hosted Proxmox VE environment. See
[architecture.md](architecture.md) for locked technical decisions.

## Stakeholders

| Role | Interest |
| --- | --- |
| Developer | Fast local feedback, easy testing, clear contribution flow |
| Ops / SRE | Reliable, observable, recoverable deployments |
| Security | No leaked secrets, HTTPS, least privilege, scanned images |
| Jury / assessor | Functional product demonstrating the required competencies |

## Functional Requirements

### Application
- FR-A1: Expose an HTTP API through FastAPI.
- FR-A2: Read and write persistent data in PostgreSQL.
- FR-A3: Provide a `/health` endpoint reporting application and DB readiness.

### Developer
- FR-D1: Run the full stack locally with a single documented command.
- FR-D2: Run an automated test suite locally and in CI.
- FR-D3: Follow a defined Git branch and review workflow.

### Ops / SRE
- FR-O1: Deploy to staging and production through automated pipelines.
- FR-O2: Reach the application over public HTTPS via Traefik.
- FR-O3: View centralized metrics, logs, dashboards, and alerts.
- FR-O4: Back up and restore the database from documented procedures.

### Security
- FR-S1: Keep all secrets out of version control.
- FR-S2: Protect operational interfaces (e.g. Traefik dashboard) with auth.
- FR-S3: Scan images and dependencies for known vulnerabilities in CI.

## Non-Functional Requirements

- NFR-1 (Reproducibility): Every environment is reproducible from
  version-controlled IaC, CaC, and manifests — no manual click-ops.
- NFR-2 (Security): Production traffic is HTTPS only; HTTP redirects to HTTPS.
- NFR-3 (Isolation): Development, staging, and production are isolated at the
  VM/cluster level with distinct credentials and DNS.
- NFR-4 (Persistence): Database data survives container/pod restarts.
- NFR-5 (Recoverability): A tested backup can be restored within a documented
  procedure (target RTO/RPO to be set; see open items below).
- NFR-6 (Observability): Health, metrics, and logs are centrally available;
  alerts fire for downtime, high error rate, resource pressure, and cert expiry.
- NFR-7 (Automation): Code changes are validated (lint + test + scan) before
  any deployment; production requires an explicit approval gate.
- NFR-8 (Documentation): Install, operate, and demo procedures are written and
  rehearsed from a clean environment before the defense.

## Resolved Decisions (were open questions)

- Cloud provider / host → **self-hosted Proxmox VE**.
- Production runtime → **k3s (Kubernetes) on Proxmox VMs**.
- SCM + CI/CD → **GitHub + GitHub Actions**.
- Environments → **dev (local Compose) + staging + production (k3s)**.
- Database → **self-hosted PostgreSQL in-cluster** (not managed).

## Remaining Open Items

- Concrete uptime / RTO / RPO targets realistic for the project scope.
- DNS strategy and domain(s) for staging vs. production.
- Container image registry (GitHub Container Registry vs. self-hosted).
- Where backups are stored (in-cluster PVC, MinIO on Proxmox, or external).
- Primary dashboard audience and the 3–4 panels each role needs.
