#!/usr/bin/env python3
"""Setup script that enforces virtual environment usage."""

import subprocess
import sys
import os


def run_command(command):
    """Execute a shell command and handle errors."""
    try:
        print(f"Running: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as cmd_error:
        print(f"Error: {cmd_error}")
        sys.exit(1)


def check_venv():
    """Check if we're running in a virtual environment."""
    if not hasattr(sys, 'real_prefix') and not (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    ):
        print("ERROR: Not running in a virtual environment!")
        print("Please activate your virtual environment first:")
        print("  source ~/venv/bin/activate")
        sys.exit(1)
    print("✓ Running in virtual environment")


def setup_development():
    """Set up development environment."""
    print("Setting up Python development environment...")
    
    # Check if we're in a venv
    check_venv()
    
    # Install requirements
    run_command("pip install -r requirements.txt")
    
    # Run linting
    run_command("pylint wsl_ubuntu_start.py")
    
    print("✓ Development environment ready!")


if __name__ == "__main__":
    setup_development()
