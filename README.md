# Supply Chain Security CI/CD Pipeline

A production-grade CI/CD pipeline demonstrating complete supply chain security for on-prem OpenStack deployment.

## What This Pipeline Does

### Layer 1: Supply Chain Security
- **Container Signing**: Cosign keyless signing (GitHub OIDC authenticated)
- **SBOM Generation**: Dual-format (SPDX + CycloneDX)
- **Attestations**: Cryptographic binding of SBOMs to images
- **Transparency**: Automatic recording to Rekor transparency log

### Layer 2: Zero-Trust Architecture
- **SHA256 Pinning**: All tools and images pinned to digest
- **SBOM Verification**: SBOMs cryptographically verified
- **Policy Enforcement**: Kubernetes admission control ready (ClusterImagePolicy)
- **Signature Validation**: Only verified images can deploy

### Layer 3: Operational Resilience
- **Chaos Engineering**: Network latency and load testing
- **SLA Validation**: Breaking point identification (< 100ms network latency)
- **Performance Baseline**: Metrics for production monitoring

## Security Scanning

Every build includes:
- **SAST**: Semgrep (policy-driven static analysis)
- **SCA**: OSV Scanner (dependency vulnerability scanning)
- **Secrets**: Gitleaks (committed credential detection)
- **Container**: Trivy (image + config scanning)
- **Infrastructure**: Goss (runtime validation)
- **SBOM**: Syft (software component inventory)
- **Tests**: Pytest (functional validation)

## Evidence & Audit Trail

- Container signatures recorded in Rekor transparency log
- SBOMs attached to images as cryptographic attestations
- All reports packaged with SHA256 checksums
- Complete forensic trail for compliance (CRA 2027 ready)

## Zero-Trust Design

All tools are pinned to SHA256 digests:
- No reliance on mutable tags
- Reproducible builds
- Supply chain integrity verified at every step

## Architecture

```
app-template/
├── .github/workflows/
│   └── ci-cd-pipeline.yaml          [→ 449 lines, 4 jobs]
├── app/
│   ├── main.py                      [FastAPI endpoints]
│   ├── config.py                    [12-Factor configuration]
│   └── routers/health.py            [K8s health checks]
├── tests/
│   └── test_main.py                 [Pytest suite]
├── scripts/
│   └── chaos_sla.py                 [Chaos engineering + SLA tests]
├── helm/
│   └── dnsdb-proxy/                 [K8s deployment charts]
├── Dockerfile                       [Hardened, non-root runtime]
└── README.md
```

## Key Metrics (From Chaos Testing)

- **Baseline response**: 50ms (healthy)
- **Network latency tolerance**: < 100ms (SLA constraint)
- **Load scaling**: Linear (1 to 20 concurrent users)
- **Bandwidth tolerance**: Handles 64 kbps (extremely resilient)

## For On-Prem Migration

This pipeline is designed for environments like OpenStack with Ceph storage:
- ✓ Validates app behavior under realistic on-prem latency (50-100ms)
- ✓ Identifies SLA breaking points before go-live
- ✓ Enables zero-trust deployments in K8s
- ✓ Provides compliance-ready audit trails

## Getting Started

See `.github/workflows/ci-cd-pipeline.yaml` for the complete implementation.
