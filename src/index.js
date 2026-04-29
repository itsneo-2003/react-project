$SyncConnector = Get-ADSyncConnector | Where-Object { $_.Name -notmatch ' - aad' }
$Zone1Partition = $SyncConnector.Partitions | Where-Object { $_.Name -match "zone1" }

$IncludedOUs = $Zone1Partition.ConnectorPartitionScope.ContainerInclusionList | Where-Object { $_ -match "^OU=" }
$ExcludedOUs = $Zone1Partition.ConnectorPartitionScope.ContainerExclusionList

$Zone1OUs = Get-ADOrganizationalUnit -Filter * -SearchBase "DC=zone1,DC=scbdev,DC=net" -SearchScope Subtree -Server "zone1.scbdev.net" |
    Select-Object -ExpandProperty DistinguishedName |
    Where-Object {
        $current = $_
        $isExcluded = $ExcludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        $isIncluded = $IncludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        -not $isExcluded -or $isIncluded
    }

$Zone1OUs | Sort-Object | Get-Unique
