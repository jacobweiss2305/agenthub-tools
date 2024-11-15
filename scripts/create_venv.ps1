# create_venv.ps1

# Remove existing venv if it exists
if (Test-Path "venv") {
    Write-Host "Removing existing venv..."
    Remove-Item -Recurse -Force "venv"
}

# Create new venv
Write-Host "Creating new virtual environment..."
python -m venv venv

# Activate venv
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate

# Install package in editable mode with dev dependencies
Write-Host "Installing package and dependencies..."
pip install -e ".[dev]"

Write-Host "Setup complete! Virtual environment is activated and ready to use."