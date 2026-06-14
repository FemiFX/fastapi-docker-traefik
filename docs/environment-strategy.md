# Environment Strategy

## Environments

| Environment | Purpose | Expected Deployment |
| --- | --- | --- |
| Development | Local development and fast feedback | Docker Compose (local) |
| Staging | Production-like validation before release | k3s on Proxmox VM(s) |
| Production | Final user-facing demo environment | k3s on Proxmox VM(s) |

Staging and production are isolated at the VM/cluster level. Each has its own
credentials, secrets, and DNS. Provisioning is via Terraform (Proxmox provider);
configuration via Ansible/cloud-init; application deployment via Kustomize
overlays applied by GitHub Actions. See [architecture.md](architecture.md).

## Configuration Principles

- Keep environment-specific values outside committed source files.
- Use `.env.example` to document required variables.
- Use CI/CD secrets or a secret manager for sensitive values.
- Keep development defaults convenient and production values explicit.

## Required Environment Variables

See `.env.example` in the repository root.
