# Development Guide for aibeehive

## Publishing Process

### Prerequisites
- PyPI account
- TestPyPI account
- GitHub account
- Repository secrets set up:
  - `PYPI_API_TOKEN` (from pypi.org)
  - `TEST_PYPI_API_TOKEN` (from test.pypi.org)

### Release Process

1. **Start New Development**
```bash
# Create new feature branch
git checkout main
git pull
git checkout -b feature/your-feature-name

# Make your changes
# Test your changes locally
pip install -e .
```

2. **Prepare for Release**
```bash
# Update version in pyproject.toml
# Example: version = "0.0.3"

# Commit changes
git add .
git commit -m "feat: your changes"
git push origin feature/your-feature-name

# Create and merge PR to main
# Then:
git checkout main
git pull
```

3. **Release**
```bash
# Create and push test tag
# For DuckDuckGo updates
git tag duckduckgo-v0.0.2
git push origin duckduckgo-v0.0.2

# For JIRA updates
git tag jira-v0.0.2
git push origin jira-v0.0.2
```