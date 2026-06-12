# Security

## Goal

Protect application traffic, secrets, infrastructure access, and operational interfaces.

## Baseline Controls

- Use HTTPS in production.
- Keep secrets out of Git.
- Restrict exposed ports.
- Protect the Traefik dashboard.
- Use least-privilege access for users and automation.
- Scan source dependencies and container images.
- Document known risks and accepted limitations.

## Secrets

Do not commit real `.env` files, passwords, tokens, private keys, or generated certificates.

## Open Decisions

- Secret storage mechanism.
- IAM model.
- Dashboard access policy.
- Vulnerability scanning tool.
