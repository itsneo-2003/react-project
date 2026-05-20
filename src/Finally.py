# Get all baseline items from SharePoint
$BaselineItems = Get-MgSiteListItem `
    -SiteId $SiteId `
    -ListId $MasterListId `
    -ExpandProperty "fields" -All

# Create hashtable
$BaselineHash = @{}

# Populate hashtable
foreach ($Item in $BaselineItems) {

    $ConfigName  = $Item.Fields.AdditionalProperties.field_3
    $ConfigValue = $Item.Fields.AdditionalProperties.field_5

    # Skip blank rows
    if (![string]::IsNullOrWhiteSpace($ConfigName)) {
        $BaselineHash[$ConfigName] = $ConfigValue
    }
}

# Test
Write-Host "TLS Baseline Value:" -ForegroundColor Cyan
$BaselineHash["TLS"]





# Get current deletion threshold
$CurrentDeletionThreshold =
$Data.value.configuration.accidentalDeletionPrevention.alertThreshold

# Get baseline value from hashtable
$BaselineDeletionThreshold =
$BaselineHash["DeletionThreshold"]

# Compare
if (
    [int]$CurrentDeletionThreshold -eq
    [int]$BaselineDeletionThreshold
) {

    Write-Host "Deletion Threshold is Compliant" `
    -ForegroundColor Green
}
else {

    Write-Host "Deletion Threshold is Non Compliant" `
    -ForegroundColor Red

    Write-Host "Current: $CurrentDeletionThreshold"
    Write-Host "Baseline: $BaselineDeletionThreshold"
}






# Get current Global Settings value
$CurrentGlob = ($GlobValue -replace '\s', '').Trim()

# Get baseline Global Settings value
$BaselineGlob = (
    $BaselineHash["Global Settings"] `
    -replace '\s', ''
).Trim()

# Compare
if ($CurrentGlob -eq $BaselineGlob) {

    Write-Host "Global Settings is Compliant" `
    -ForegroundColor Green
}
else {

    Write-Host "Global Settings is Non Compliant" `
    -ForegroundColor Red

    Write-Host "Current Value:"
    Write-Host $GlobValue

    Write-Host ""
    Write-Host "Baseline Value:"
    Write-Host $BaselineHash["Global Settings"]
}




# Normalize both values
$CurrentGlob = ($GlobValue -replace '\s', '').Trim()
$BaselineGlob = (
    $BaselineHash["Global Settings"] `
    -replace '\s', ''
).Trim()

# Compare line by line
Compare-Object `
    ($CurrentGlob -split "`r?`n") `
    ($BaselineGlob -split "`r?`n")
















function Test-ControlCompliance {

    param (
        [string]$ConfigName
    )

    # Get values
    $CurrentValue = $CurrentHash[$ConfigName]
    $BaselineValue = $BaselineHash[$ConfigName]

    # Check for missing values
    if ($null -eq $CurrentValue -or
        $null -eq $BaselineValue) {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host ""
        Write-Host "$ConfigName : Missing value" `
        -ForegroundColor Red

        return
    }

    # Normalize
    # Remove spaces/tabs
    # Ignore case
    # Keep new lines

    $CurrentNormalized = (
        $CurrentValue.ToString().ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    $BaselineNormalized = (
        $BaselineValue.ToString().ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    # Compare
    if ($CurrentNormalized -eq
        $BaselineNormalized) {

        $StatusHash[$ConfigName] = "Compliant"

        Write-Host "$ConfigName : Compliant" `
        -ForegroundColor Green
    }
    else {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host "$ConfigName : Non Compliant" `
        -ForegroundColor Red
    }
}







$CurrentHash["TLS"] = $FormattedTLS
Test-ControlCompliance -ConfigName "TLS"






function Test-ControlCompliance {

    param (
        [string]$ConfigName
    )

    # Get values
    $CurrentValue = $CurrentHash[$ConfigName]
    $BaselineValue = $BaselineHash[$ConfigName]

    # Check missing values
    if ($null -eq $CurrentValue -or
        $null -eq $BaselineValue) {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host "$ConfigName : Missing value" `
        -ForegroundColor Red

        return
    }

    # Convert to string
    $CurrentNormalized = $CurrentValue.ToString()
    $BaselineNormalized = $BaselineValue.ToString()

    # Normalize line endings
    $CurrentNormalized = $CurrentNormalized `
        -replace "`r`n", "`n"

    $BaselineNormalized = $BaselineNormalized `
        -replace "`r`n", "`n"

    # Remove spaces/tabs only
    # Ignore case
    # Keep new lines

    $CurrentNormalized = (
        $CurrentNormalized.ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    $BaselineNormalized = (
        $BaselineNormalized.ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    # Compare
    if ($CurrentNormalized -eq
        $BaselineNormalized) {

        $StatusHash[$ConfigName] = "Compliant"

        Write-Host "$ConfigName : Compliant" `
        -ForegroundColor Green
    }
    else {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host "$ConfigName : Non Compliant" `
        -ForegroundColor Red

        Write-Host ""
        Write-Host "Mismatch found in: $ConfigName" `
        -ForegroundColor Yellow

        Compare-Object `
            ($CurrentNormalized -split "`n") `
            ($BaselineNormalized -split "`n")
    }
}






function Test-ControlCompliance {

    param (
        [string]$ConfigName,

        [string[]]$IgnoreFields = @()
    )

    # Get values
    $CurrentValue = $CurrentHash[$ConfigName]
    $BaselineValue = $BaselineHash[$ConfigName]

    # Check missing values
    if ($null -eq $CurrentValue -or
        $null -eq $BaselineValue) {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host ""
        Write-Host "$ConfigName : Missing value" `
        -ForegroundColor Red

        return
    }

    # Convert to string
    $CurrentValue = $CurrentValue.ToString()
    $BaselineValue = $BaselineValue.ToString()

    # Remove ignored fields
    if ($IgnoreFields.Count -gt 0) {

        foreach ($Field in $IgnoreFields) {

            $CurrentValue = (
                $CurrentValue -split "`r?`n" |
                Where-Object {
                    $_ -notmatch "^$Field\s*:"
                }
            ) -join "`n"

            $BaselineValue = (
                $BaselineValue -split "`r?`n" |
                Where-Object {
                    $_ -notmatch "^$Field\s*:"
                }
            ) -join "`n"
        }
    }

    # Normalize line endings
    $CurrentNormalized = (
        $CurrentValue `
        -replace "`r`n", "`n"
    )

    $BaselineNormalized = (
        $BaselineValue `
        -replace "`r`n", "`n"
    )

    # Ignore spaces/tabs
    # Ignore case
    # Keep new lines

    $CurrentNormalized = (
        $CurrentNormalized.ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    $BaselineNormalized = (
        $BaselineNormalized.ToLower() `
        -replace '[ \t]', ''
    ).Trim()

    # Compare
    if ($CurrentNormalized -eq
        $BaselineNormalized) {

        $StatusHash[$ConfigName] = "Compliant"

        Write-Host "$ConfigName : Compliant" `
        -ForegroundColor Green
    }
    else {

        $StatusHash[$ConfigName] = "Non Compliant"

        Write-Host "$ConfigName : Non Compliant" `
        -ForegroundColor Red
    }
}



$CurrentHash["AD Sync Scheduler"] =
$FormattedADSync

Test-ControlCompliance `
-ConfigName "AD Sync Scheduler" `
-IgnoreFields @(
    "NextSyncCycleStartTimeInUTC",
    "SyncCycleInProgress"
)
