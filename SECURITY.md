# Security

Do not publish secrets, credentials, private local paths, wallet material, customer data, private memory, or internal-only strategy in this repository.

Report security concerns through the GitHub repository security channel or a private maintainer contact.

<!-- STARLIGHT-REPO-CONTRACT:START -->
## Starlight repository contract

Contract: `starlight.repo_profile.v2` · Team: `starlight-platform-team` · Priority: `now`
### Data boundary

- Classification: `public`
- PII allowed in product-owned storage: `false`
- Auth owner: `None`

Never read or print `.env` values. Keep secrets in approved secret stores, keep PII out of analytics events and receipts, scan untrusted code before execution, and stop on credential or private-memory exposure.
<!-- STARLIGHT-REPO-CONTRACT:END -->
