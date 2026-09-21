param(
    [ValidateSet('Apply','Remove')]
    [string]$Mode = 'Apply'
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..\..')).Path
$codexHome = (Resolve-Path -LiteralPath (Join-Path $env:USERPROFILE '.codex')).Path
$sandboxGroup = "$env:COMPUTERNAME\CodexSandboxUsers"
$sandboxSid = ([System.Security.Principal.NTAccount]$sandboxGroup).Translate([System.Security.Principal.SecurityIdentifier])
foreach ($path in @($repoRoot, $codexHome)) {
    $acl = Get-Acl -LiteralPath $path
    if ($Mode -eq 'Apply') {
        $exists = $acl.Access | Where-Object {
            $_.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value -eq $sandboxSid.Value -and
            $_.AccessControlType -eq [System.Security.AccessControl.AccessControlType]::Deny -and
            (($_.FileSystemRights -band [System.Security.AccessControl.FileSystemRights]::ReadAndExecute) -ne 0) -and
            $_.InheritanceFlags -eq ([System.Security.AccessControl.InheritanceFlags]::ContainerInherit -bor [System.Security.AccessControl.InheritanceFlags]::ObjectInherit)
        }
        if (-not $exists) {
            & icacls.exe $path /deny "*$($sandboxSid.Value):(OI)(CI)(RX)" | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "icacls deny failed for $path (exit $LASTEXITCODE)" }
        }
    } else {
        & icacls.exe $path /remove:d "*$($sandboxSid.Value)" | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "icacls deny removal failed for $path (exit $LASTEXITCODE)" }
    }
}

# Verify that the Owner identity still has access after either operation.
Get-ChildItem -LiteralPath $repoRoot -ErrorAction Stop | Select-Object -First 1 | Out-Null
Get-ChildItem -LiteralPath $codexHome -ErrorAction Stop | Select-Object -First 1 | Out-Null
Write-Output "mode=$Mode"
Write-Output "sandbox_group=$sandboxGroup"
Write-Output "repo_root=$repoRoot"
Write-Output "codex_home=$codexHome"
