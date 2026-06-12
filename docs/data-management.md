# Data Management

## Goal

Make PostgreSQL storage persistent, recoverable, and documented.

## Baseline Requirements

- Database data must survive container restarts.
- Database credentials must come from environment variables or secrets.
- Backup and restore procedures must be documented.
- Backup and restore must be tested before the final demo.

## Backup Strategy

To define after the deployment target is selected.

## Restore Strategy

To define after the deployment target is selected.

## Open Decisions

- Self-hosted PostgreSQL or managed database.
- Backup location.
- Backup frequency.
- Recovery time and recovery point expectations.
