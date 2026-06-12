# Environment Strategy

## Environments

| Environment | Purpose | Expected Deployment |
| --- | --- | --- |
| Development | Local development and fast feedback | Docker Compose |
| Staging | Production-like validation before release | To define |
| Production | Final user-facing demo environment | To define |

## Configuration Principles

- Keep environment-specific values outside committed source files.
- Use `.env.example` to document required variables.
- Use CI/CD secrets or a secret manager for sensitive values.
- Keep development defaults convenient and production values explicit.

## Required Environment Variables

See `.env.example` in the repository root.
