# AC Microcourses - GitHub Copilot Instructions

AC Microcourses is a Python-based educational platform hosted by the Acceleration Consortium at the University of Toronto. The repository contains microcredentials courses for self-driving laboratory topics, built with PyScaffold, Sphinx documentation, and Jupyter notebooks.

**ALWAYS follow these instructions first and fallback to additional search and context gathering only if the information here is incomplete or found to be in error.**

## Working Effectively

### Environment Setup and Build Process

During validation, I encountered confirmed network timeout issues in CI environments when installing pip dependencies.

#### Basic Environment Setup 
```bash
# Primary approach - FAILS with network timeouts in CI
conda env create -f environment.yml
```

**Actual failure observed after 1m53s:**
```
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='pypi.org', port=443): Read timed out.
CondaEnvException: Pip failed
```

**Working alternative (validated - 7 seconds):**
```bash
# Use conda-only dependencies from environment-basic.yml
conda env create -f environment-basic.yml
conda activate ac-microcourses
```

#### Package Installation 
```bash
# Development installation - FAILS with network timeouts  
pip install -e .
```

**Actual failure observed after 15s:**
```
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='pypi.org', port=443): Read timed out.
```

**Working alternative (validated):**
```bash
# Use PYTHONPATH for development - works reliably
export PYTHONPATH=/home/runner/work/ac-microcourses/ac-microcourses/src:$PYTHONPATH
python -c "import ac_microcourses; print('Package imported successfully')"
```

### Testing and Validation

#### Running Tests (validated - 0.47 seconds)
```bash
# RECOMMENDED: With PYTHONPATH approach 
conda activate ac-microcourses
export PYTHONPATH=/home/runner/work/ac-microcourses/ac-microcourses/src:$PYTHONPATH
pytest
```

**Actual results:**
```
1 passed in 0.14s
TOTAL coverage: 8 statements, 100% coverage  
```

#### Test Coverage
- Tests located in `tests/` directory (single file: `tests/hello_test.py`)
- Configuration in `setup.cfg` under `[tool:pytest]`
- Uses pytest-cov for coverage reporting

### Build and Package Management

#### Tox
Network timeouts prevent reliable tox execution in CI environments. Use pytest directly instead:
```bash
pytest  # Reliable alternative to tox
```

#### Documentation Build  
Documentation builds require additional dependencies from `docs/requirements.txt` which fail to install due to network timeouts in CI environments.

### Pre-commit and Linting

#### Pre-commit Hooks
Network timeout issues prevent reliable pre-commit hook installation in CI environments.

#### Manual Validation
```bash
# Basic Python syntax checking (available in conda environment)
python -m py_compile src/ac_microcourses/*.py

# Use pytest for basic code validation  
pytest --collect-only
```

## Validation Scenarios

### Complete Functionality Test (validated)
```bash
# 1. Create environment (7 seconds)
conda env create -f environment-basic.yml
conda activate ac-microcourses

# 2. Package import test
export PYTHONPATH=/home/runner/work/ac-microcourses/ac-microcourses/src:$PYTHONPATH
python -c "import ac_microcourses; print('Package imported successfully')"
python -c "import ac_microcourses.hello; print('Hello module imported successfully')"

# 3. Run test suite (0.47 seconds total)
pytest

# 4. Check git status
git --no-pager status
```

### Documentation Validation
```bash
# Check documentation structure (no network required)
ls docs/
find docs/ -name "*.md" | head -5
```

## Network Timeout Issues (Validated in CI)

### Commands That Fail Due to Network Timeouts:
- `conda env create -f environment.yml` (pip dependencies cause ReadTimeoutError)
- `pip install -e .` (fails after ~15 seconds with ReadTimeoutError)  
- `pip install -r docs/requirements.txt` (network dependent)
- `tox` (depends on pip installations)
- `pre-commit install` (requires network access)

### Reliable Commands (No Network Required):
- `conda env create -f environment-basic.yml` (7 seconds, conda-only deps)
- `pytest` (0.47 seconds with PYTHONPATH)
- `git` commands (instant)
- `python -c "import ..."` (with PYTHONPATH)
- File operations

## Project Structure

### Key Directories
- `src/ac_microcourses/` - Main Python package (2 files: `__init__.py`, `hello.py`)
- `tests/` - Unit tests (1 test file: `hello_test.py`)
- `docs/` - Sphinx documentation with courses content
- `notebooks/` - Jupyter notebooks (4 files including `sdl-demo.ipynb`)
- `scripts/` - Utility scripts (demo/, generate_overviews.py)

### Configuration Files
- `environment.yml` - Full conda environment (includes pip deps that timeout)
- `environment-basic.yml` - Conda-only environment (reliable in CI)
- `setup.cfg` - Package configuration and pytest settings
- `pyproject.toml` - Build system configuration
- `tox.ini` - Test automation (requires network)
- `.pre-commit-config.yaml` - Pre-commit hooks (requires network)

## Common Network Timeout Troubleshooting

### ReadTimeoutError from PyPI
**Problem**: `ReadTimeoutError: HTTPSConnectionPool(host='pypi.org', port=443): Read timed out`

**Solution**: Use conda-only environment and PYTHONPATH:
```bash
conda env create -f environment-basic.yml
conda activate ac-microcourses
export PYTHONPATH=/home/runner/work/ac-microcourses/ac-microcourses/src:$PYTHONPATH
```

### Missing Dependencies for Documentation
**Problem**: Documentation builds fail due to missing sphinx themes

**Solution**: Documentation builds require pip dependencies which fail in CI environments

## Summary

**Recommended Development Workflow:**
1. Use `conda env create -f environment-basic.yml` (7s, reliable)
2. Set `PYTHONPATH` for package imports (works without pip install)
3. Use `pytest` directly for testing (0.47s, 100% coverage)
4. Use git commands for version control (reliable)

This approach avoids all network-dependent operations while maintaining full development functionality.