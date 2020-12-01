$total = 0
$found = @{}
$match = $false
$continue = $true

while($match -eq $false)
{
    foreach($line in Get-content .\freq.txt)
    {
        $total += [int]$line
        if(!$found.ContainsKey($total))
        {
            $found.Add($total, 1)
        }
        else
        {
            Write-Host "Frequency Found!"
            Write-Host $total
            $match = $true
            break
        }
    }
    if($continue)
    {
        Write-Host $total
        $continue = $false
    }
}
