function Test-ControlCompliance {

    param (

        [string]$ConfigName,

        [string[]]$IgnoreFields = @(),

        [string[]]$IgnoreBlocks = @()

    )

    # Get values
    $CurrentValue = $CurrentHash[$ConfigName]

    $BaselineValue = $BaselineHash[$ConfigName]

    # Check missing values
    if ($null -eq $CurrentValue -or
        $null -eq $BaselineValue) {

        $StatusHash[$ConfigName] =
        "Non Compliant"

        Write-Host ""

        Write-Host "$ConfigName : Missing value" `
        -ForegroundColor Red

        return
    }

    # Convert to string
    $CurrentValue =
    $CurrentValue.ToString()

    $BaselineValue =
    $BaselineValue.ToString()

    # Remove ignored fields
    if ($IgnoreFields.Count -gt 0) {

        foreach ($Field in $IgnoreFields) {

            $CurrentValue = (

                $CurrentValue -split "`r?`n" |

                Where-Object {

                    $_ -notmatch
                    "^$Field\s*:"

                }

            ) -join "`n"

            $BaselineValue = (

                $BaselineValue -split "`r?`n" |

                Where-Object {

                    $_ -notmatch
                    "^$Field\s*:"

                }

            ) -join "`n"
        }
    }

    # Remove ignored JSON blocks
    if ($IgnoreBlocks.Count -gt 0) {

        foreach ($BlockName in
            $IgnoreBlocks) {

            $Pattern =
            '(?s)\{.*?"Name"\s*:\s*"' +
            [regex]::Escape(
                $BlockName
            ) +
            '".*?\}'

            $CurrentValue =
            [regex]::Replace(

                $CurrentValue,

                $Pattern,

                ''

            )

            $BaselineValue =
            [regex]::Replace(

                $BaselineValue,

                $Pattern,

                ''

            )
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

        $CurrentNormalized
        .ToLower() `
        -replace '[ \t]', ''

    ).Trim()

    $BaselineNormalized = (

        $BaselineNormalized
        .ToLower() `
        -replace '[ \t]', ''

    ).Trim()

    # Compare
    if ($CurrentNormalized -eq
        $BaselineNormalized) {

        $StatusHash[$ConfigName] =
        "Compliant"

        Write-Host
        "$ConfigName : Compliant" `
        -ForegroundColor Green
    }
    else {

        $StatusHash[$ConfigName] =
        "Non Compliant"

        Write-Host
        "$ConfigName : Non Compliant" `
        -ForegroundColor Red
    }
}
