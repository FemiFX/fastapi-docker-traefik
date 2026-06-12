# Project Goals and Delivery Plan

## 1. Project Context

This project uses the `fastapi-docker-traefik` repository as the base application for a DevOps and Cloud Architecture training project. The current implementation provides a small FastAPI service, a PostgreSQL database, Docker Compose definitions for development and production, and Traefik as the reverse proxy and HTTPS entry point.

The target is to evolve this prototype into a documented, automated, secure, observable, and reproducible multi-environment deployment. The final result should demonstrate practical DevOps skills across application packaging, infrastructure automation, CI/CD, security, data management, monitoring, and operational readiness.

## 2. Current Starting Point

The repository currently includes:

- FastAPI application in `app/`
- PostgreSQL database integration using `databases`, `ormar`, and SQLAlchemy
- Development Docker Compose setup in `docker-compose.yml`
- Production Docker Compose setup in `docker-compose.prod.yml`
- Traefik development and production configuration
- Basic production HTTPS support through Traefik and Let's Encrypt
- Minimal README with local and production startup commands

This is a good foundation for the application and containerization layer, but it still needs project documentation, automated tests, CI/CD, infrastructure automation, stronger secret handling, environment separation, observability, backup/restore procedures, and deployment hardening.

## 3. Main Goals

The project should achieve the following outcomes:

- Deliver a functional FastAPI application deployed through containers.
- Support separate environments such as development, staging, and production.
- Automate build, test, delivery, and deployment workflows through CI/CD.
- Use Everything as Code principles:
  - Infrastructure as Code for cloud resources.
  - Configuration as Code for services and environments.
  - Pipeline as Code for integration and deployment.
- Secure application traffic with HTTPS.
- Protect credentials and configuration through secret management.
- Provide database persistence, backup, and restore procedures.
- Add monitoring, logging, health checks, and alerts.
- Document installation, operations, architecture, and demo steps.
- Prepare a final presentation and live demo that clearly shows the system working.

## 4. Success Criteria

The project can be considered successful when:

- A user can run the application locally from documented instructions.
- The application can be deployed to at least one remote environment.
- The deployment is reproducible from version-controlled configuration.
- CI/CD automatically validates code changes before deployment.
- Secrets are not hardcoded in source-controlled files.
- The production entry point uses HTTPS.
- Database data survives container restarts.
- Backup and restore procedures are documented and tested.
- Logs and metrics are available from a central place.
- Dashboards and alerts exist for the main operational concerns.
- The final demo can show application access, deployment workflow, infrastructure, database persistence, and monitoring.

## 5. Recommended Tooling

### Application and Runtime

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- Docker
- Docker Compose
- Traefik

### Testing and Quality

- `pytest` for unit and integration tests
- `httpx` or FastAPI `TestClient` for API tests
- Ruff or Flake8 for linting
- Black for formatting
- Bandit for Python security checks
- Trivy for container image and dependency scanning

### CI/CD

Choose one CI/CD platform and keep it consistent:

- GitHub Actions, if the repository is hosted on GitHub
- GitLab CI, if the repository is hosted on GitLab

Recommended pipeline stages:

- Lint
- Unit tests
- Build container image
- Security scan
- Push image to registry
- Deploy to staging
- Run smoke tests
- Promote or deploy to production

### Infrastructure and Cloud

Recommended options:

- Terraform for Infrastructure as Code
- Ansible for server configuration, if using VMs
- Docker Compose for a simple VM-based deployment
- Kubernetes, Helm, or Kustomize if the project expands to orchestration
- Cloud provider of choice: AWS, Azure, GCP, OVHcloud, Scaleway, or another training-approved provider

### Security

- Traefik HTTPS with Let's Encrypt
- Environment-specific `.env` files excluded from Git
- Cloud secret manager, GitHub Actions secrets, GitLab CI variables, or SOPS
- Least-privilege IAM users and roles
- Basic authentication or stronger access control for Traefik dashboard
- Restricted database access

### Observability

Recommended stack for a self-managed deployment:

- Prometheus for metrics
- Grafana for dashboards
- Loki or an ELK/OpenSearch stack for logs
- Alertmanager for alerts
- Application `/health` endpoint
- Traefik access logs and metrics

For a managed cloud approach, equivalent managed logging, metrics, and alerting services can be used.

## 6. Recommended Project Phases

### Phase 0: Framing and Scope

Objective: define what will be delivered and what will intentionally stay out of scope.

Tasks:

- Confirm stakeholders and expectations.
- Define the target demo scenario.
- Decide the deployment target: local VM, cloud VM, Kubernetes, or managed service.
- Decide the CI/CD platform.
- Create an initial backlog and milestones.

Deliverables:

- Project scope
- Initial backlog
- High-level architecture direction
- Initial risk list

### Phase 1: Specifications and Repository Organization

Objective: turn the project brief into practical architecture and implementation specifications.

Tasks:

- Document functional and non-functional requirements.
- Define environments: development, staging, production.
- Document repository structure.
- Define Git workflow and branch strategy.
- Add architecture diagrams.
- Define application, database, reverse proxy, CI/CD, infrastructure, and monitoring components.

Deliverables:

- Requirements document
- Architecture document
- Environment strategy
- Git and contribution workflow
- Initial diagrams

### Phase 2: Application Hardening and Tests

Objective: make the FastAPI prototype reliable enough to automate.

Tasks:

- Add health check endpoint.
- Add automated API tests.
- Add database integration tests where practical.
- Add linting and formatting.
- Improve configuration management.
- Replace hardcoded production credentials with environment variables or secrets.
- Review production Traefik labels and dashboard routing.

Deliverables:

- Test suite
- Health endpoint
- Improved configuration
- Updated README

### Phase 3: CI/CD Pipeline

Objective: automate validation and deployment workflows.

Tasks:

- Add pipeline definition.
- Run linting and tests on each pull request or merge request.
- Build Docker image automatically.
- Scan image and dependencies.
- Push versioned image to a registry.
- Deploy automatically to staging.
- Add manual approval or protected deployment for production.
- Add smoke tests after deployment.

Deliverables:

- Pipeline as Code
- Automated image build
- Automated staging deployment
- Documented production release process

### Phase 4: Infrastructure Automation

Objective: provision the target runtime environment reproducibly.

Tasks:

- Define cloud account/project structure.
- Create network, firewall, compute, DNS, and storage resources with IaC.
- Configure server or cluster access.
- Install required runtime components.
- Configure Traefik entry points and certificates.
- Define environment-specific variables and secrets.

Deliverables:

- Infrastructure as Code
- Configuration as Code
- Documented provisioning procedure
- Remote environment ready for deployment

### Phase 5: Data Management

Objective: make PostgreSQL persistence operationally safe.

Tasks:

- Define database storage strategy.
- Configure persistent volumes or managed database storage.
- Add backup script or managed backup policy.
- Add restore procedure.
- Test backup and restore.
- Define access controls for database users.

Deliverables:

- Database persistence strategy
- Backup procedure
- Restore procedure
- Backup/restore test evidence

### Phase 6: Security Hardening

Objective: reduce operational and exposure risks.

Tasks:

- Remove hardcoded credentials from Compose files.
- Store secrets outside Git.
- Enforce HTTPS in production.
- Protect Traefik dashboard.
- Restrict exposed ports.
- Add image and dependency scanning.
- Define least-privilege access for users, CI/CD, and infrastructure.
- Document security assumptions and remaining risks.

Deliverables:

- Secure configuration baseline
- Secret management approach
- Security checklist
- Vulnerability scan reports

### Phase 7: Observability

Objective: make the system measurable and diagnosable.

Tasks:

- Add application health endpoint.
- Enable Traefik access logs.
- Add metrics collection.
- Add centralized log collection.
- Create dashboards for app, database, proxy, and host or cluster.
- Define alert rules for downtime, high error rate, resource pressure, and certificate issues.

Deliverables:

- Monitoring stack
- Dashboards
- Alert rules
- Operational runbook

### Phase 8: Final Demo and Defense Preparation

Objective: prepare a clear, repeatable demonstration for the jury.

Tasks:

- Write installation and deployment instructions.
- Prepare demo script.
- Prepare presentation slides.
- Show application access through Traefik.
- Show CI/CD pipeline execution.
- Show deployed infrastructure.
- Show database persistence and backup/restore.
- Show monitoring dashboard and alerts.
- Document known limitations and future improvements.

Deliverables:

- Final README
- Demo script
- Slides
- Working deployed application
- Final architecture and operations documentation

## 7. Suggested Documentation Set

Recommended files to add under `docs/`:

- `requirements.md`
- `architecture.md`
- `environment-strategy.md`
- `ci-cd.md`
- `infrastructure.md`
- `security.md`
- `data-management.md`
- `observability.md`
- `runbook.md`
- `demo-script.md`

These documents do not need to be long at first. They should start as practical notes and become more complete as each phase is implemented.

## 8. Initial Technical Backlog

Priority items:

- Add `.env.example` for required variables.
- Remove hardcoded database credentials from Compose files.
- Add `/health` endpoint to FastAPI.
- Add automated API tests.
- Add linting and formatting configuration.
- Add CI pipeline.
- Add image scanning.
- Fix and validate production Traefik dashboard routing.
- Add backup and restore scripts for PostgreSQL.
- Add basic monitoring and logging documentation.

Later improvements:

- Add staging and production deployment separation.
- Add Terraform infrastructure.
- Add Ansible server configuration or Kubernetes manifests.
- Add Prometheus and Grafana.
- Add centralized logging.
- Add blue/green or canary deployment strategy.
- Add disaster recovery documentation.

## 9. Key Risks and Decisions

Open decisions:

- Which cloud provider will host the project?
- Will production run on Docker Compose, Kubernetes, or a managed container platform?
- Which CI/CD platform will be used?
- Will PostgreSQL be self-hosted or managed?
- Which monitoring stack will be used?

Risks:

- The project scope can become too large for the available time.
- Kubernetes may add unnecessary complexity if the deadline is tight.
- Hardcoded secrets and dashboard exposure can weaken the security assessment.
- Observability and backup work can be delayed if left until the end.
- A live demo can fail if deployment steps are not rehearsed and documented.

Recommended mitigation:

- Deliver a working Docker Compose production path first.
- Add automation and hardening incrementally.
- Keep all procedures documented as they are implemented.
- Rehearse the final demo from a clean environment before the defense.

## 10. Recommended Minimum Viable Demo

The minimum strong demo should show:

- A code change merged through the chosen Git workflow.
- CI pipeline running tests and building the image.
- Deployment to a remote staging or production environment.
- Public HTTPS access through Traefik.
- FastAPI returning data from PostgreSQL.
- Persistent database data after container restart.
- Backup and restore demonstration or evidence.
- Monitoring dashboard showing service health and logs.

This scope is realistic, demonstrates the required DevOps competencies, and leaves room for bonus improvements such as IaC, autoscaling, advanced monitoring, canary deployments, and disaster recovery.
