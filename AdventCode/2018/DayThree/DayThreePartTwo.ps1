$total = 0
$field = @{}

Write-Host "ARRAY MADE"
foreach($line in Get-content .\day3.txt)
{
    $match = $true
    $processed = $line.Split("@,:")
    $area = $processed[3].Split("x")
    $x = [int]$processed[3].Split("x")[0]
    $y = [int]$processed[3].Split("x")[1]
    $left = [int]$processed[1]
    $top = [int]$processed[2]
    for($i = $left; $i -lt ($x + $left); $i++)
    {
        for($j = $top; $j -lt ($y + $top); $j++)
        {
            $key = "$i, $j"
            if(!$field.ContainsKey($key))
            {
                $field.Add($key, 1)
            }
            else
            {
                $field[$key] = 2
                $match = $false
            }
        }
    }
}
Write-Host "FILE PROCESSED"
for($i = 0; $i -lt 1000; $i++)
{
    for($j = 0; $j -lt 1000; $j++)
    {
        $key = "$i, $j"
        if($field.ContainsKey($key) -and $field[$key] -eq 2)
        {
            $total++
        }
    }
}
Write-Host $total
#new code for section two
foreach($line in Get-content .\day3.txt)
{
    $match = $true
    $processed = $line.Split("@,:")
    $area = $processed[3].Split("x")
    $x = [int]$processed[3].Split("x")[0]
    $y = [int]$processed[3].Split("x")[1]
    $left = [int]$processed[1]
    $top = [int]$processed[2]
    for($i = $left; $i -lt ($x + $left); $i++)
    {
        for($j = $top; $j -lt ($y + $top); $j++)
        {
            $key = "$i, $j"
            if($field[$key] -eq 2)
            {
                $match = $false
            }
        }
    }
    if($match -eq $true)
    {
        Write-Host $processed
    }
}
