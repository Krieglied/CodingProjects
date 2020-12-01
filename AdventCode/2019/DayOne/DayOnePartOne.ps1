$totalfuel = Get-Content .\day1.txt
$sumfuel = 0

foreach ($fuel in $totalfuel)
{
    $sumfuel += [math]::floor($fuel / 3) - 2    
}
$sumfuel
