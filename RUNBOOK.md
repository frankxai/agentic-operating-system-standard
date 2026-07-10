# agentic-operating-system-standard — Runbook

<!-- STARLIGHT-REPO-CONTRACT:START -->
## Starlight repository contract

Contract: `starlight.repo_profile.v2` · Team: `starlight-platform-team` · Priority: `now`
### Fast gates

- health: `npm run validate`
- lint: not applicable
- typecheck: not applicable
- test: `npm run validate`
- build: not applicable
- security: `pwsh ../security/Invoke-RepoSecurityScan.ps1 -Path .`

### Release

Classify risk, run applicable gates locally, use one coherent preview when deployed, obtain an independent verifier verdict, record evidence, and confirm rollback before promotion. Only predesignated low-risk web changes may use green automatic promotion.
<!-- STARLIGHT-REPO-CONTRACT:END -->
