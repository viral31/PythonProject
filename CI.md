# CI / GitHub Actions

This repository includes a GitHub Actions workflow at `.github/workflows/jab.yml` that runs a secure CI pipeline on push and pull requests.

What the workflow does
- Checkout code
- Set up Python 3.11
- Install dependencies from `requirements.txt`
- Lint with `flake8` (non-blocking)
- Run tests with `pytest` (non-blocking)
- Run SonarQube analysis (requires `SONAR_TOKEN` secret)
- Run CodeQL analysis
- Run OWASP ZAP baseline scan (requires `ZAP_TARGET` secret for target URL)
- Build Docker image and run Trivy container scan

Required repository secrets
- `SONAR_TOKEN` — token for SonarQube / SonarCloud.
- `ZAP_TARGET` — (optional) URL for OWASP ZAP to scan (e.g., staging URL).

Local checks
1. Create a virtualenv and install deps:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install pytest flake8
```

2. Run lint and tests:

```cmd
flake8
pytest -q
```

Notes
- The workflow runs some steps non-blocking (lint/tests) to keep the example simple. You can make them fail the job by removing the `|| true` from the workflow steps.
- Update the `IMAGE_NAME` value in the workflow if you want a different Docker image tag.
- Configure the repository secrets in GitHub Settings → Secrets & variables → Actions.
