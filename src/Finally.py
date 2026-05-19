Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $TransactionListId |
Select Name, DisplayName




      
Get-MgSiteListColumn `
    -SiteId $SiteId `
    -ListId $MasterListId |
Select Name, DisplayName




        # ============================
# TLS Control (BP-002)
# ============================

$RefNumber = "BP-002"

# Get transaction item
$TransactionItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# Get baseline item
$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# Current TLS value
$CurrentTLS = ($FormattedTLS).Trim()

# Baseline TLS value
$BaselineTLS = (
    $BaselineItem.Fields.AdditionalProperties.field_5
).Trim()

# Compliance check
if ($CurrentTLS -eq $BaselineTLS) {
    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"
}

# Update transaction list
$Body = @{
    field_5 = $CurrentTLS
    Status = $ComplianceStatus
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TransactionItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

Write-Host "TLS Updated Successfully"
Write-Host "Status: $ComplianceStatus"







# ============================
# TLS Control (BP-002)
# ============================

$RefNumber = "BP-002"

# ----------------------------
# Get current TLS value
# ----------------------------

$key = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client"

if (Test-Path $key) {
    $TLS = Get-ItemProperty $key
}
else {
    Write-Host "TLS 1.2 Registry key not found"
    return
}

# Convert TLS object to multiline text
$FormattedTLS = (
    $TLS.PSObject.Properties |
    ForEach-Object {
        "$($_.Name): $($_.Value)"
    }
) -join "`r`n"

# ----------------------------
# Get transaction item
# ----------------------------

$TransactionItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" `
    -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# ----------------------------
# Get baseline item
# ----------------------------

$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" `
    -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq $RefNumber
}

# ----------------------------
# Normalize current TLS
# ----------------------------

$CurrentTLS = (
    ($FormattedTLS -replace '\r\n', "`n") `
    -replace '\s+', ' '
).Trim()

# ----------------------------
# Normalize baseline TLS
# ----------------------------

$BaselineTLS = (
    (
        $BaselineItem.Fields.AdditionalProperties.field_5 `
        -replace '\r\n', "`n"
    ) -replace '\s+', ' '
).Trim()

# Debug check
Write-Host "Current Length: $($CurrentTLS.Length)"
Write-Host "Baseline Length: $($BaselineTLS.Length)"

# ----------------------------
# Compliance check
# ----------------------------

if ($CurrentTLS -eq $BaselineTLS) {
    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"
}

Write-Host "Compliance Status: $ComplianceStatus"

# ----------------------------
# Update transaction row
# ----------------------------

$Body = @{
    field_5 = $FormattedTLS
    Status = $ComplianceStatus
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TransactionItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

Write-Host "TLS Row Updated Successfully"





# ==========================================
# TLS CONTROL (BP-002)
# ==========================================

# Get TLS row from transaction list
$TLSItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $TransactionListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-002"
}

# Get current review count
$CurrentReview = $TLSItem.Fields.AdditionalProperties.Review

if ([string]::IsNullOrEmpty($CurrentReview)) {
    $NewReview = 1
}
else {
    $NewReview = [int]$CurrentReview + 1
}

# Current timestamp
$LastRunDateTime = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")

# ==========================================
# GET BASELINE TLS
# ==========================================

$BaselineItem = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All |
Where-Object {
    $_.Fields.AdditionalProperties.field_2 -eq "BP-002"
}

$BaselineText = $BaselineItem.Fields.AdditionalProperties.field_5

# ==========================================
# EXTRACT CURRENT TLS VALUES
# ==========================================

$CurrentEnabled = $TLS.Enabled
$CurrentDisabled = $TLS.DisabledByDefault

# ==========================================
# EXTRACT BASELINE TLS VALUES
# ==========================================

$BaselineEnabled = [regex]::Match(
    $BaselineText,
    'Enabled\s*:\s*(\d+)'
).Groups[1].Value

$BaselineDisabled = [regex]::Match(
    $BaselineText,
    'DisabledByDefault\s*:\s*(\d+)'
).Groups[1].Value

# ==========================================
# COMPLIANCE CHECK
# ==========================================

if (($CurrentEnabled -eq $BaselineEnabled) -and
    ($CurrentDisabled -eq $BaselineDisabled)) {

    $ComplianceStatus = "Compliant"
}
else {
    $ComplianceStatus = "Non Compliant"
}

# ==========================================
# UPDATE TRANSACTION LIST
# ==========================================

$Body = @{
    Review = $NewReview
    LastRunDateTime = $LastRunDateTime
    Status = $ComplianceStatus
    field_5 = $FormattedTLS
} | ConvertTo-Json

Invoke-MgGraphRequest `
    -Method PATCH `
    -Uri "https://graph.microsoft.com/v1.0/sites/$SiteId/lists/$TransactionListId/items/$($TLSItem.Id)/fields" `
    -Body $Body `
    -ContentType "application/json"

Write-Host "TLS Updated Successfully"
Write-Host "Status: $ComplianceStatus"
Write-Host "Review Number: $NewReview"
Write-Host "LastRunDateTime: $LastRunDateTime"
