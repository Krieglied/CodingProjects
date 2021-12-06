$fishes = Get-Content .\DaySix\day6_input.txt
$fish_bins = 0,0,0,0,0,0,0,0,0
foreach($fish in $fishes.Split(','))
{
    $fish_bins[[int]$fish]++
}
for($i = 1; $i -le 256; $i++)
{
    $previous = $fish_bins[8]
    $tmp = 0
    $fish_bins[8] = $fish_bins[0]

    $tmp = $fish_bins[7]
    $fish_bins[7] = $previous

    $previous = $fish_bins[6]
    $fish_bins[6] = $tmp + $fish_bins[0]

    $tmp = $fish_bins[5]
    $fish_bins[5] = $previous

    $previous = $fish_bins[4]
    $fish_bins[4] = $tmp

    $tmp = $fish_bins[3]
    $fish_bins[3] = $previous

    $previous = $fish_bins[2]
    $fish_bins[2] = $tmp

    $tmp = $fish_bins[1]
    $fish_bins[1] = $previous

    $previous = $fish_bins[0]
    $fish_bins[0] = $tmp

    
}
$sum = 0
foreach($bin in $fish_bins)
{
    $sum += $bin
}
Write-Host "Day " $i "has " $sum " number of fish"