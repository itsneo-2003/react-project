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





$SyncConnector = Get-ADSyncConnector | Where-Object { $_.Name -notmatch ' - aad' }
$Zone2Partition = $SyncConnector.Partitions | Where-Object { $_.Name -match "zone2" }

$IncludedOUs = $Zone2Partition.ConnectorPartitionScope.ContainerInclusionList | Where-Object { $_ -match "^OU=" }
$ExcludedOUs = $Zone2Partition.ConnectorPartitionScope.ContainerExclusionList

$Zone2OUs = Get-ADOrganizationalUnit -Filter * -SearchBase "DC=zone2,DC=scbdev,DC=net" -SearchScope Subtree -Server "zone2.scbdev.net" |
    Select-Object -ExpandProperty DistinguishedName |
    Where-Object {
        $current = $_
        $isExcluded = $ExcludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        $isIncluded = $IncludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        -not $isExcluded -or $isIncluded
    }

$Zone2OUs | Sort-Object | Get-Unique






$SyncConnector = Get-ADSyncConnector | Where-Object { $_.Name -notmatch ' - aad' }
$Zone3Partition = $SyncConnector.Partitions | Where-Object { $_.Name -match "zone3" }

$IncludedOUs = $Zone3Partition.ConnectorPartitionScope.ContainerInclusionList | Where-Object { $_ -match "^OU=" }
$ExcludedOUs = $Zone3Partition.ConnectorPartitionScope.ContainerExclusionList

$Zone3OUs = Get-ADOrganizationalUnit -Filter * -SearchBase "DC=zone3,DC=scbdev,DC=net" -SearchScope Subtree -Server "zone3.scbdev.net" |
    Select-Object -ExpandProperty DistinguishedName |
    Where-Object {
        $current = $_
        $isExcluded = $ExcludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        $isIncluded = $IncludedOUs | Where-Object { $current -eq $_ -or $current -like "*,$_" }
        -not $isExcluded -or $isIncluded
    }

$Zone3OUs | Sort-Object | Get-Unique
