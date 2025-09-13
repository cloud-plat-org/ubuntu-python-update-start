"""Ubuntu setup script for WSL with cloud environment detection."""
import subprocess
import requests  # pylint: disable=import-error

def run_command(command):
    """Execute a shell command and handle errors."""
    try:
        print(f"Running: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as cmd_error:
        print(f"Error: {cmd_error}")


def detect_cloud():
    """Detect if running on AWS, Azure, or local environment."""
    try:
        # AWS metadata service
        response = requests.get('http://169.254.169.254/latest/meta-data/', timeout=2)
        if response.status_code == 200:
            return 'aws'
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        pass

    try:
        # Azure metadata service
        response = requests.get('http://169.254.169.254/metadata/instance?api-version=2021-02-01',
                              headers={'Metadata': 'true'}, timeout=2)
        if response.status_code == 200:
            return 'azure'
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        pass

    return 'local'

if __name__ == "__main__":
    # Install essential development tools
    run_command("sudo apt install -y git python3-requests")

    CLOUD_ENV = detect_cloud()
    print(f"Cloud environment: {CLOUD_ENV}")

    if CLOUD_ENV == 'aws':
        run_command("curl -fsSL https://apt.amazonaws.com/gpg | "
                   "sudo gpg --dearmor -o /usr/share/keyrings/aws-archive-keyring.gpg")
        run_command("echo \"deb [signed-by=/usr/share/keyrings/aws-archive-keyring.gpg] "
                   "https://apt.amazonaws.com/ubuntu $(lsb_release -cs) main\" | "
                   "sudo tee /etc/apt/sources.list.d/aws.list")
        run_command("sudo apt update")
        run_command("sudo apt upgrade -y")
    elif CLOUD_ENV == 'azure':
        run_command("curl -sL https://packages.microsoft.com/keys/microsoft.asc | "
                   "gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null")
        run_command("sudo apt update")
        run_command("sudo apt upgrade -y")
        run_command("sudo apt install -y azure-cli")
    else:
        # You may want to add the deadsnakes PPA for latest versions
        run_command("sudo apt install -y software-properties-common")
        run_command("sudo add-apt-repository -y ppa:deadsnakes/ppa")
        run_command("sudo apt update")
        run_command("sudo apt upgrade -y")
        run_command("sudo apt install -y python3 python3-dev python3-venv")

    # Ensure pip3 is installed and upgraded in the virtual environment
    run_command("python3 -m venv ~/venv")
    run_command("~/venv/bin/pip install --upgrade pip")
    run_command("source ~/venv/bin/activate && python3 --version")
    run_command("~/venv/bin/python --version")
    run_command("~/venv/bin/pip --version")

    # Install pylint
    run_command("~/venv/bin/pip install pylint")
    run_command("~/venv/bin/pylint --version")
    run_command("~/venv/bin/pylint wsl_ubuntu_start.py")
