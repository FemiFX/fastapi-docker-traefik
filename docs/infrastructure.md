# Infrastructure

## Goal

Provision and configure all runtime infrastructure reproducibly using Infrastructure as Code and Configuration as Code.

## Target Resources

- Cloud project or account.
- Network and firewall rules.
- Compute runtime: VM, Kubernetes cluster, or managed container service.
- DNS records.
- Persistent database storage or managed database.
- TLS certificate handling.
- Monitoring and logging resources.

## Recommended Tools

- Terraform for cloud infrastructure.
- Ansible for VM configuration if using virtual machines.
- Docker Compose for simple VM-based deployment.
- Helm or Kustomize if Kubernetes is selected.

## Open Decisions

- Cloud provider.
- Runtime platform.
- Network layout.
- DNS provider.
- Storage and backup strategy.
