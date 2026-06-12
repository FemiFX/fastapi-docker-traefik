# Requirements

## Purpose

Define the functional and non-functional requirements that will guide architecture, implementation, deployment, and defense decisions.

## Functional Requirements

- The application exposes an HTTP API through FastAPI.
- The application stores and reads persistent data from PostgreSQL.
- The application can be run locally for development.
- The application can be deployed to a remote environment.
- The application is reachable through Traefik.

## Non-Functional Requirements

- Deployment must be reproducible from source-controlled files.
- Production traffic must use HTTPS.
- Secrets must not be committed to Git.
- The system must support separate development, staging, and production environments.
- The system must provide basic health visibility.
- Backup and restore procedures must exist for persistent data.

## Open Questions

- What is the final cloud provider?
- What is the final production runtime: Docker Compose, Kubernetes, or managed containers?
- What uptime and recovery expectations are realistic for the project scope?
- Which users or stakeholders should the monitoring dashboards target?
