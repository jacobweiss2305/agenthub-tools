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

3. **Test Release (TestPyPI)**
```bash
# Create and push test tag
git tag v0.0.3-test
git push origin v0.0.3-test

# Wait for GitHub Actions to complete
# Check: https://github.com/jacobweiss2305/aibeehive/actions

# Verify on TestPyPI
# Check: https://test.pypi.org/project/aibeehive/

# Test installation
pip install -i https://test.pypi.org/simple/ aibeehive==0.0.3
```

4. **Production Release (PyPI)**
```bash
# If test was successful, create production tag
git tag v0.0.3
git push origin v0.0.3

# Wait for GitHub Actions to complete
# Check: https://github.com/jacobweiss2305/aibeehive/actions

# Verify on PyPI
# Check: https://pypi.org/project/aibeehive/

# Test installation
pip install aibeehive==0.0.3
```

### Troubleshooting

If a release fails:
```bash
# Delete local tag
git tag -d v0.0.3

# Delete remote tag
git push --delete origin v0.0.3

# Fix issues and try again
```

### Version Numbering

Follow semantic versioning:
- PATCH (0.0.X) for bug fixes
- MINOR (0.X.0) for new features
- MAJOR (X.0.0) for breaking changes

### Quick Commands Reference

```bash
# Check existing tags
git tag -l

# Delete test tag if needed
git tag -d v0.0.3-test
git push --delete origin v0.0.3-test

# Delete prod tag if needed
git tag -d v0.0.3
git push --delete origin v0.0.3
```

## Current GitHub Actions

The repository has two workflows:
1. `publish_testpypi.yml`: Triggered by `v*-test` tags
2. `publish_pypi.yml`: Triggered by `v*` tags (excluding test tags)

## Notes for Future Me
- Always test on TestPyPI first
- Remember to update version in pyproject.toml
- Wait for test workflow to complete before pushing prod tag
- Check Actions tab if something fails