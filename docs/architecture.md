# Jenkins CI/CD Automation Lab — Architecture

## End-to-end flow

Developer
-> Git repository
-> Jenkins controller
-> Validate
-> Test
-> Docker build
-> Quality gate
-> Artifact/image publication
-> Environment deployment
-> Smoke verification
-> Rollback when verification fails

## Component responsibilities

| Component | Responsibility |
|---|---|
| Git | Source control and pipeline trigger |
| Jenkins | Orchestration, stages, credentials and promotion |
| Validation/Test | Fast feedback before packaging |
| Docker | Immutable application packaging |
| SonarQube | Static analysis / quality gate integration point |
| Nexus/Registry | Artifact and image storage integration point |
| Deployment target | Runs the promoted release |
| Verification | Confirms the deployed version is healthy |
| Rollback | Restores the previous known-good release |

## Security and production hardening

- Keep credentials in Jenkins Credentials; never in the repository.
- Restrict production deployment to approved branches/environments.
- Add SonarQube webhook-based quality gates.
- Publish images/artifacts to an approved registry or Nexus.
- Add vulnerability scanning and SBOM generation.
- Add audit logging and deployment approvals.
- Export pipeline duration, success/failure and deployment metrics to Prometheus/Grafana.

The implementation is deliberately generic so it can be demonstrated publicly without exposing company infrastructure.
