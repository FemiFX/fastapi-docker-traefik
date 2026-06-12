# CI/CD

## Goal

Automate validation, packaging, security scanning, and deployment of the application and supporting infrastructure.

## Recommended Pipeline Stages

1. Lint and format check.
2. Run unit and API tests.
3. Build Docker image.
4. Scan dependencies and container image.
5. Push image to registry.
6. Deploy to staging.
7. Run smoke tests.
8. Deploy or promote to production with approval.

## Open Decisions

- CI/CD platform: GitHub Actions or GitLab CI.
- Container registry location.
- Deployment target and credentials model.
- Production approval process.
