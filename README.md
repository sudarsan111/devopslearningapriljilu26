# DevOps Learning Repository (April 2026)

This repository is dedicated to learning and practicing fundamental DevOps concepts, including version control, containerization, and Continuous Integration/Continuous Deployment (CI/CD).

## Project Overview

- **Python Applications**: Basic Python scripts (`app.py`, `helloworld.py`) for testing and containerization.
- **Containerization**: A `Dockerfile` is included to demonstrate how to containerize a basic Python application.
- **CI/CD Pipeline**: A GitHub Actions workflow (`ci.yml`) is configured to run automated checks on pull requests and pushes to the `main` branch. This includes:
  - Unit testing using `pytest`
  - Linting using `ruff`
  - Security scanning using `bandit`
- **Git Practice**: Various text files used for practicing basic Git commands, branching, and pushing changes.

## Getting Started

To run the containerized application locally:

1. Build the Docker image:
   ```bash
   docker build -t devops-python-app .
   ```
2. Run the Docker container:
   ```bash
   docker run devops-python-app
   ```