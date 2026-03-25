$url = "https://config.zscaler.com/zscloud.net/cenr"

# Fetch page content
$response = Invoke-WebRequest -Uri $url

# Extract IPv4 CIDR ranges using regex
$ipv4Ranges = ($response.Content | Select-String -Pattern '\b(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}\b' -AllMatches).Matches.Value

# Remove duplicates (just in case)
$ipv4Ranges = $ipv4Ranges | Sort-Object -Unique

# Output
$ipv4Ranges
