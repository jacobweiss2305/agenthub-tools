# format_code.ps1

# Activate venv if not already activated
if (-not ($env:VIRTUAL_ENV)) {
    .\venv\Scripts\Activate
}

Write-Host "Formatting code with black..."
black hive/
black examples/
isort hive/
isort examples/

if ($LASTEXITCODE -eq 0) {
    Write-Host "Code formatting complete!" -ForegroundColor Green
} else {
    Write-Host "Code formatting failed. Please check the errors above." -ForegroundColor Red
}