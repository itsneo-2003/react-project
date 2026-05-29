function Compare-SyncedOUs {

    param (
        [string]$ConfigName
    )

    $CurrentValue =
    $CurrentHash[$ConfigName]

    $BaselineValue =
    $BaselineHash[$ConfigName]

    # Convert multiline strings to arrays
    $CurrentOUs =
    $CurrentValue `
    -split "`r?`n" |
    Where-Object {
        $_.Trim() -ne ""
    } |
    ForEach-Object {
        $_.Trim()
    }

    $BaselineOUs =
    $BaselineValue `
    -split "`r?`n" |
    Where-Object {
        $_.Trim() -ne ""
    } |
    ForEach-Object {
        $_.Trim()
    }

    # Find added and removed OUs
    $AddedOUs =
    $CurrentOUs |
    Where-Object {
        $_ -notin $BaselineOUs
    }

    $RemovedOUs =
    $BaselineOUs |
    Where-Object {
        $_ -notin $CurrentOUs
    }

    # Compliance check
    if (
        $AddedOUs.Count -eq 0 -and
        $RemovedOUs.Count -eq 0
    ) {

        $StatusHash[$ConfigName] =
        "Compliant"

        Write-Host
        Write-Host `
        "$ConfigName : Compliant" `
        -ForegroundColor Green

        return
    }

    $StatusHash[$ConfigName] =
    "Non Compliant"

    Write-Host
    Write-Host `
    "$ConfigName : Non Compliant" `
    -ForegroundColor Red

    if ($AddedOUs.Count -gt 0) {

        Write-Host
        Write-Host `
        "Added OUs:" `
        -ForegroundColor Yellow

        $AddedOUs |
        ForEach-Object {

            Write-Host $_ `
            -ForegroundColor Cyan
        }
    }

    if ($RemovedOUs.Count -gt 0) {

        Write-Host
        Write-Host `
        "Removed OUs:" `
        -ForegroundColor Yellow

        $RemovedOUs |
        ForEach-Object {

            Write-Host $_ `
            -ForegroundColor Magenta
        }
    }
}
