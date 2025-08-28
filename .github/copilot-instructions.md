# AC Microcourses - GitHub Copilot Instructions

AC Microcourses is a Python-based educational platform hosted by the Acceleration Consortium at the University of Toronto. The repository contains microcredentials courses for self-driving laboratory topics, built with PyScaffold, Sphinx documentation, and Jupyter notebooks.

**ALWAYS follow these instructions first and fallback to additional search and context gathering only if the information here is incomplete or found to be in error.**

## Working Effectively

### Environment Setup and Build Process (NETWORK ISSUES COMMON)

**CRITICAL: Network timeouts to PyPI are common in CI environments. NEVER CANCEL builds that appear to hang - they may take 15+ minutes.**

#### Basic Environment Setup (36 seconds - validated)
```bash
# Create conda environment (takes ~36 seconds)
conda env create -f environment.yml  # OFTEN FAILS due to pip network timeouts

# Alternative: Create basic environment without pip dependencies
conda env create -f /tmp/environment-basic.yml  # Use this if main env fails
conda activate ac-microcourses
```

**NEVER CANCEL**: Environment creation can take 2-15 minutes depending on network conditions. Set timeout to 20+ minutes.

#### Package Installation (NETWORK ISSUES EXPECTED)
```bash
# Development installation - OFTEN FAILS due to network timeouts
pip install -e .  # Expected to fail in CI due to PyPI timeouts

# Alternative: Use PYTHONPATH for development
export PYTHONPATH=/path/to/ac-microcourses/src:$PYTHONPATH
```

**Network Timeout Workaround**: If pip installations fail with "Read timed out" errors, use the PYTHONPATH approach instead.

### Testing and Validation (0.5 seconds - validated)

#### Running Tests
```bash
# Method 1: With PYTHONPATH (RECOMMENDED for network issues)
export PYTHONPATH=/path/to/ac-microcourses/src:$PYTHONPATH
pytest  # Takes ~0.5 seconds

# Method 2: Standard approach (if pip install worked)
pytest
```

#### Test Coverage
- Tests are located in `tests/` directory
- Single test file: `tests/hello_test.py`
- Configuration in `setup.cfg` under `[tool:pytest]`
- Uses pytest-cov for coverage reporting

### Build and Package Management

#### Tox (NETWORK TIMEOUTS EXPECTED)
```bash
# OFTEN FAILS due to network timeouts
tox  # Expected failure: "pip._vendor.urllib3.exceptions.ReadTimeoutError"

# Alternative: Run tests directly
pytest
```

**NEVER CANCEL**: Tox may take 30-60 minutes when network is slow. Set timeout to 90+ minutes.

#### Documentation Build (REQUIRES ADDITIONAL DEPENDENCIES)
```bash
# Install docs dependencies (OFTEN FAILS due to network)
pip install -r docs/requirements.txt  # Expected to timeout

# Basic sphinx attempt (will fail due to missing themes)
cd docs/
sphinx-build -b html . _build/html
```

**Documentation Dependencies**: The build requires sphinx_book_theme and other packages from `docs/requirements.txt`. In network-constrained environments, documentation builds will fail.

### Pre-commit and Linting (NETWORK ISSUES)

#### Pre-commit Hooks
```bash
# Installation often fails due to network timeouts
pre-commit install  # May timeout during hook installation
pre-commit run --all-files  # Expected to fail: "ReadTimeoutError"
```

#### Manual Linting (LIMITED TOOLS AVAILABLE)
```bash
# Basic Python syntax checking
python -m py_compile src/ac_microcourses/*.py

# Pytest includes some basic checks
pytest --collect-only
```

**Linting Limitation**: flake8, black, and isort are not available in basic conda environment. Pre-commit hooks require network access to install.

## Validation Scenarios

### Basic Functionality Test
```bash
# 1. Environment activation
conda activate ac-microcourses

# 2. Package import test
export PYTHONPATH=/path/to/ac-microcourses/src:$PYTHONPATH
python -c "import ac_microcourses; print('Package imported successfully')"
python -c "import ac_microcourses.hello; print('Hello module imported successfully')"

# 3. Run test suite
pytest  # Should complete in <1 second

# 4. Check git status
git --no-pager status  # Should complete in <1 second
```

### Documentation Validation (LIMITED)
```bash
# Check documentation structure
ls docs/
find docs/ -name "*.md" | head -5
```

## Network Timeout Reference

### Commands That OFTEN FAIL Due to Network Issues:
- `conda env create -f environment.yml` (pip dependencies)
- `pip install -e .`
- `pip install -r docs/requirements.txt`
- `tox`
- `pre-commit install`
- `pre-commit run --all-files`

### Working Commands (No Network Required):
- `conda env create -f environment-basic.yml` (conda-only deps)
- `pytest` (with PYTHONPATH)
- `git` commands
- `python -c "import ..."` (with PYTHONPATH)
- Basic file operations

## Project Structure

### Key Directories
- `src/ac_microcourses/` - Main Python package (2 files: `__init__.py`, `hello.py`)
- `tests/` - Unit tests (1 test file: `hello_test.py`)
- `docs/` - Sphinx documentation with courses content
- `notebooks/` - Jupyter notebooks (4 files including `sdl-demo.ipynb`)
- `scripts/` - Utility scripts (demo/, generate_overviews.py)

### Configuration Files
- `environment.yml` - Conda environment (includes pip deps that may timeout)
- `setup.cfg` - Package configuration and pytest settings
- `pyproject.toml` - Build system configuration
- `tox.ini` - Test automation (may timeout)
- `.pre-commit-config.yaml` - Pre-commit hooks (requires network)

### CI/CD
- `.github/workflows/ci.yml` - GitHub Actions workflow
- Uses pipx, pre-commit, and tox (all network-dependent)

## Timing Expectations

### Fast Operations (<5 seconds)
- `pytest` - 0.5 seconds
- `git status` - <0.1 seconds
- Python imports - <0.1 seconds
- File listings - <0.1 seconds

### Medium Operations (30 seconds - 5 minutes)
- `conda env create` (conda-only) - 36 seconds
- Basic conda package installations

### Slow Operations (5-60+ minutes) - NEVER CANCEL
- `conda env create -f environment.yml` - 2-15 minutes (often fails)
- `tox` - 30-60 minutes (often fails)
- `pre-commit run --all-files` - 5-30 minutes (often fails)
- `pip install` operations - 1-15 minutes (often fails)

## Common Troubleshooting

### Network Timeout Errors
**Problem**: "ReadTimeoutError: HTTPSConnectionPool(host='pypi.org', port=443): Read timed out"

**Solution**: Use conda-only environment and PYTHONPATH approach:
```bash
# Use basic environment
conda env create -f /tmp/environment-basic.yml
conda activate ac-microcourses
export PYTHONPATH=/path/to/ac-microcourses/src:$PYTHONPATH
```

### Missing Sphinx Themes
**Problem**: "Could not import extension sphinx_book_theme"

**Solution**: Documentation builds require additional dependencies from `docs/requirements.txt` which often fail to install due to network issues.

### Pre-commit Hook Failures
**Problem**: Pre-commit hooks fail to install

**Solution**: Use manual validation approaches or skip pre-commit in network-constrained environments.

## Critical Reminders

- **NEVER CANCEL**: Builds and package installations may take 60+ minutes
- **Network issues are normal**: Expect pip timeouts in CI environments
- **Use PYTHONPATH workaround**: When pip install fails
- **Set long timeouts**: 90+ minutes for builds, 30+ minutes for tests
- **Test core functionality**: Import tests and pytest are reliable validators
- **Document limitations**: Note network dependency failures in any instructions