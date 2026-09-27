# Architecture

The pipeline validates source, runs tests, builds an immutable Docker image, applies quality gates, publishes an artifact, deploys to a selected environment, and verifies the deployment.

## Production hardening
- Store credentials in Jenkins Credentials.
- Add SonarQube webhook quality gates.
- Publish images/artifacts to Nexus or an approved registry.
- Add vulnerability scanning and SBOM generation.
- Require approvals for production promotion.
- Add Prometheus/Grafana metrics for pipeline duration and failure rate.
