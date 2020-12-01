$total = 0

foreach($line in Get-content .\freq.txt)
{
    $total += [int]$line
}
Write-Host $total
