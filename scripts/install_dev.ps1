param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Packages,
    
    [switch]$NoEditable,
    
    [switch]$Force,
    
    [switch]$UpgradePip
)

# Function to handle the pip installation process
function Install-Package {
    param(
        [string]$PackagePath,
        [string]$PackageName,
        [bool]$Editable = $true
    )
    
    Write-Host "Installing $PackageName..." -ForegroundColor Cyan
    
    try {
        if ($Editable) {
            pip install -e $PackagePath $(if ($Force) { "--force-reinstall" })
        } else {
            pip install $PackagePath $(if ($Force) { "--force-reinstall" })
        }
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Successfully installed $PackageName" -ForegroundColor Green
        } else {
            Write-Host "Failed to install $PackageName" -ForegroundColor Red
            exit 1
        }
    }
    catch {
        Write-Host "Error installing $PackageName : $_" -ForegroundColor Red
        exit 1
    }
}

# Upgrade pip if requested
if ($UpgradePip) {
    Write-Host "Upgrading pip..." -ForegroundColor Cyan
    python -m pip install --upgrade pip
}

# If no packages specified, get all package directories
if (-not $Packages) {
    $Packages = Get-ChildItem -Path "packages" -Directory | Select-Object -ExpandProperty Name
}

# Validate all packages exist before starting installation
$invalidPackages = $Packages | Where-Object { -not (Test-Path "packages/$_") }
if ($invalidPackages) {
    Write-Host "Error: The following packages were not found:" -ForegroundColor Red
    $invalidPackages | ForEach-Object { Write-Host "  - $_" }
    exit 1
}

# Always install core first if it's in the list
if ($Packages -contains "core") {
    $Packages = @("core") + ($Packages | Where-Object { $_ -ne "core" })
}

# Display installation plan
Write-Host "`nInstallation Plan:" -ForegroundColor Yellow
Write-Host "- Mode: $(if ($NoEditable) { 'Regular' } else { 'Editable (-e)' })"
Write-Host "- Force reinstall: $Force"
Write-Host "- Packages to install:" -NoNewline
$Packages | ForEach-Object { Write-Host "`n  - $_" }
Write-Host ""

# Install each package
foreach ($package in $Packages) {
    $packagePath = "packages/$package"
    Install-Package -PackagePath $packagePath -PackageName $package -Editable (-not $NoEditable)
}

Write-Host "`nAll packages installed successfully!" -ForegroundColor Green