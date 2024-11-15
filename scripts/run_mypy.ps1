# run_mypy.ps1

# Activate venv if not already activated
if (-not ($env:VIRTUAL_ENV)) {
    .\venv\Scripts\Activate
}

Write-Host "Running mypy type checks..."
mypy ghostrade/

if ($LASTEXITCODE -eq 0) {
    Write-Host "Type checking passed!" -ForegroundColor Green
} else {
    Write-Host "Type checking failed. Please fix the issues above." -ForegroundColor Red
}