param(
    [Parameter(Mandatory=$false)]
    [string]$dep
)

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

# Install package in editable mode with dependencies
Write-Host "Installing package and dependencies..."
if ($dep) {
    Write-Host "Installing with dev and $dep dependencies..."
    pip install -e ".[dev,$dep]"
} else {
    Write-Host "Installing with dev dependencies only..."
    pip install -e ".[dev]"
}

Write-Host "`nAvailable dependency groups:"
Write-Host "- confluence"
Write-Host "- jira"
Write-Host "- duckduckgo"
Write-Host "- yahoo_finance"

Write-Host "`nSetup complete! Virtual environment is activated and ready to use."