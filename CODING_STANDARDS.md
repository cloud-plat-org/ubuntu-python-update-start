# Python Coding Standards

This project follows Python linting standards using pylint and enforces virtual environment usage.

## Standards Applied

- **Virtual Environments**: Always use venv for Python projects
- **Line length**: Maximum 100 characters
- **Naming conventions**:
  - Variables/functions: `snake_case`
  - Constants: `UPPER_CASE`
  - Classes: `PascalCase`
  - Modules: `snake_case`
- **Documentation**: All modules and functions should have docstrings
- **Error handling**: Use specific exception types, not bare `except:`

## Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv ~/venv

# Activate virtual environment
source ~/venv/bin/activate

# Install dependencies
pip install pylint requests

# Deactivate when done
deactivate
```

## Running Linting

```bash
# Activate virtual environment first
source ~/venv/bin/activate

# Run pylint on all Python files
pylint *.py

# Run pylint on specific file
pylint wsl_ubuntu_start.py
```

## Configuration

The project uses `.pylintrc` for configuration. Key settings:
- Max line length: 100 characters
- Requires docstrings for modules and functions
- Enforces Python naming conventions
- Limits complexity metrics

## When Recommending Code

Always ensure code follows these standards:
1. **Use virtual environments** - Never install packages globally
2. Use proper naming conventions
3. Add docstrings to functions and modules
4. Keep lines under 100 characters
5. Use specific exception handling
6. Follow PEP 8 style guidelines
7. Use `~/venv/bin/python` and `~/venv/bin/pip` in scripts
