# Ubuntu Python Development Environment Setup

A comprehensive Python development environment setup script for Ubuntu systems, with cloud environment detection and automated code quality tools.

## Overview

This project provides an automated setup script that prepares an Ubuntu system for Python development by:
- Installing essential development tools
- Detecting cloud environments (AWS, Azure, or local)
- Setting up Python virtual environments
- Installing and configuring code quality tools (pylint)
- Maintaining clean system state

## System Requirements

- **OS**: Ubuntu 24.04 (Noble Numbat)
- **Environment**: WSL2 (Windows Subsystem for Linux)
- **Python**: 3.12.3 (installed via system packages)
- **Shell**: Bash

## Quick Start

### Option 1: Download and Run (Recommended)
```bash
# Download the script directly
wget https://raw.githubusercontent.com/cloud-plat-org/ubuntu-python-update-start/first_script/wsl_ubuntu_start.py
python3 ./wsl_ubuntu_start.py
```

### Option 2: Clone Repository (if git is available)
```bash
# Clone the repository (requires git to be installed)
git clone https://github.com/cloud-plat-org/ubuntu-python-update-start.git
cd ubuntu-python-update-start

# Run the setup script
python3 ./wsl_ubuntu_start.py
```

**Note**: The script will automatically install git and other dependencies during setup.

## Project Files

### Core Scripts

- **`wsl_ubuntu_start.py`** - Main setup script that automates the entire development environment setup
- **`setup_dev.py`** - Development environment configuration helper

### Configuration Files

- **`.pylintrc`** - Pylint configuration with custom rules for code quality
- **`pyproject.toml`** - Python project configuration and metadata
- **`requirements.txt`** - Python package dependencies
- **`.gitignore`** - Git ignore patterns for Python projects

### Documentation

- **`CODING_STANDARDS.md`** - Project coding standards and guidelines
- **`LICENSE`** - MIT License for the project

## Key Features

### Cloud Environment Detection
The script automatically detects and configures the environment based on:
- **AWS**: Configures AWS repositories (CLI installation not included)
- **Azure**: Installs Azure CLI and configures Microsoft repositories  
- **Local**: Sets up deadsnakes PPA for latest Python versions

### Code Quality Integration
- **Pylint**: Comprehensive code analysis with custom configuration
- **Virtual Environment**: Isolated Python environment setup
- **Standards Compliance**: Enforces PEP 8 and project-specific standards

## Design Decisions & Improvements

### 1. Variable Naming Standards
**Issue**: Exception variable `e` didn't meet naming requirements (minimum 3 characters)
**Solution**: Renamed to `cmd_error` for better clarity and compliance
**Impact**: Improved code readability and standards compliance

### 2. Pylint Configuration Optimization
**Issue**: Invalid configuration options (`max-class-lines`, `max-function-lines`) caused errors
**Solution**: Removed unsupported options from `.pylintrc`
**Impact**: Clean pylint execution without configuration errors

### 3. Shell Compatibility Fix
**Issue**: `source` command failed in subprocess (uses `/bin/sh` by default)
**Solution**: Used `bash -c 'source ~/venv/bin/activate && python3 --version'`
**Impact**: Proper virtual environment activation verification

### 4. System Cleanup Timing ⭐
**Issue**: Unused packages (`libllvm19`) accumulated warnings throughout setup
**Solution**: Moved `apt autoremove -y` to run immediately after initial package installation
**Impact**: 
- Cleaner system state throughout setup process
- Better user experience (cleanup happens when warnings appear)
- More logical execution flow

## Technical Specifications

### Installed Software Versions
- **Python**: 3.12.3
- **Pip**: 25.2
- **Pylint**: 3.3.8
- **Astroid**: 3.3.11
- **Git**: 1:2.43.0-1ubuntu7.3
- **Requests**: 2.31.0+dfsg-1ubuntu1.1

### Virtual Environment
- **Location**: `~/venv/`
- **Python**: 3.12.3
- **Pip**: Upgraded to latest version
- **Packages**: pylint, requests (as needed)

### Code Quality Standards
- **Line Length**: Maximum 100 characters
- **Variable Names**: `snake_case`, minimum 3 characters
- **Function Names**: `snake_case`, minimum 3 characters
- **Class Names**: `PascalCase`
- **Constants**: `UPPER_CASE`

## Usage Instructions

### Basic Setup
```bash
python3 ./wsl_ubuntu_start.py
```

### Manual Virtual Environment Activation
```bash
[source ~/venv/bin/activate]
```

### Running Code Quality Checks
```bash
# Activate virtual environment
source ~/venv/bin/activate

# Run pylint on specific file
pylint wsl_ubuntu_start.py

# Run pylint on all Python files
pylint *.py
```

### Development Workflow
1. Run the setup script once to initialize the environment
2. Activate the virtual environment for development
3. Install additional packages as needed: `~/venv/bin/pip install <package>`
4. Run pylint regularly to maintain code quality

## Environment Detection Logic

The script detects the environment by attempting to access cloud metadata services:

1. **AWS Detection**: Checks `http://169.254.169.254/latest/meta-data/`
2. **Azure Detection**: Checks `http://169.254.169.254/metadata/instance?api-version=2021-02-01`
3. **Local Fallback**: If neither cloud service responds, configures for local development

## Troubleshooting

### Common Issues
- **Permission Errors**: Ensure script is run with appropriate sudo privileges
- **Network Issues**: Cloud detection requires internet connectivity
- **Package Conflicts**: Script handles existing installations gracefully

### Verification Steps
1. Check Python version: `~/venv/bin/python --version`
2. Verify pylint installation: `~/venv/bin/pylint --version`
3. Run code quality check: `~/venv/bin/pylint wsl_ubuntu_start.py`

## Development Environment Details

- **Created On**: WSL2 Ubuntu 24.04 (Noble Numbat)
- **Python Version**: 3.12.3
- **Package Manager**: apt (Ubuntu)
- **Virtual Environment**: venv (Python standard library)
- **Code Quality**: pylint 3.3.8 with custom configuration

## Contributing

1. Follow the coding standards outlined in `CODING_STANDARDS.md`
2. Ensure all code passes pylint checks (10.00/10 score)
3. Test on Ubuntu 24.04 WSL2 environment
4. Update documentation for any new features

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.