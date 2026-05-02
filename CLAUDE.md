# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest --tb=short -v

# Run tests with coverage (CI requirement: 80% minimum)
pytest --cov=. --cov-fail-under=80

# Lint
pip install ruff
ruff check .

# Security scan
pip install bandit
bandit -r src/

# Run the app locally
python app.py

# Build Docker image
docker build -t my-devops-app .

# Run Docker container locally
docker run -p 8080:5000 my-devops-app
```

## Architecture

This is a learning project for DevOps/SRE practices built around a minimal Python/Flask app.

**Key files:**
- [app.py](app.py) — entry point (currently minimal)
- [config.py](config.py) — feature flags read from environment variables (`FF_NEW_CHECKOUT`, `FF_AI_RECS`)
- [Dockerfile](Dockerfile) — uses `python:3.11`, copies and runs `app.py`
- [requirements.txt](requirements.txt) — `flask==3.0.0`, `pytest==7.4.0`

**CI/CD pipeline** ([.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml)) has 4 sequential jobs:
1. **test** — runs `pytest` + `ruff` lint on every push to `main`/`develop` and all PRs
2. **build** — builds and pushes Docker image to GitHub Container Registry (`ghcr.io`) only if tests pass; image tagged by branch, PR, SHA, and `latest` (on `main` only)
3. **deploy-staging** — SSH-deploys the `develop` image to staging on port `8080:5000`
4. **deploy-production** — SSH-deploys the `latest` image to production on port `80:5000`

Required GitHub secrets for deployment: `STAGING_HOST`, `STAGING_USER`, `STAGING_SSH_KEY`, `PROD_HOST`, `PROD_USER`, `PROD_SSH_KEY`.

## Feature Flags

Feature flags live in [config.py](config.py) and are controlled via environment variables:

```bash
FF_NEW_CHECKOUT=true   # enables new_checkout_flow
FF_AI_RECS=true        # enables ai_recommendations
```

Use `config.flag("new_checkout_flow")` to check a flag in code.

## Branch Strategy

- `main` — production; triggers build + deploy-production
- `develop` — staging; triggers build + deploy-staging
- PRs must target `main` and pass the quality gate (tests + lint + security scan with 80% coverage)
