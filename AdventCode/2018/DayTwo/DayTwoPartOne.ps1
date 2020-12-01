$found = @{}
$twos = 0
$threes = 0
foreach($line in Get-content .\freq.txt)
{
    $string = $line.ToCharArray()
    foreach($item in $string)
    {
        if(!$found.ContainsKey($item))
        {
            $found.Add($item,1)
        }
        else
        {
            $found[$item] += 1
        }
    }
    if($found.ContainsValue(2))
    {
        $twos++
    }
    if($found.ContainsValue(3))
    {
        $threes++
    }
    $found.Clear()
}

$sum = $twos * $threes
Write-Host $twos
Write-Host $threes
Write-Host $sum
