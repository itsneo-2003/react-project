Fix — Steps in Order
Step 1 — Close your current PowerShell session completely and open a fresh PowerShell 7 window (not Windows PowerShell). This clears all loaded assemblies from memory.
Step 2 — Force-install the latest versions of both modules together:
Install-Module Microsoft.Graph.Authentication -Force -AllowClobber -Scope CurrentUser
Install-Module Microsoft.Graph.Applications -Force -AllowClobber -Scope CurrentUser
Say Y or A when prompted about PSGallery.
Step 3 — Explicitly import them in the correct order (Auth first):
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Applications
Step 4 — Verify both are on the same version:
Get-Module Microsoft.Graph.Authentication, Microsoft.Graph.Applications | Select Name, Version
Both should show the same version number (e.g., 2.35.1).
Step 5 — Reconnect and retry:
Connect-MgGraph -Scopes 'ConfigurationMonitoring.ReadWrite.All'

$utcm = New-MgServicePrincipal -AppId '03b07b79-c5bc-4b5e-9bfa-13acf4a99998'
$utcm
