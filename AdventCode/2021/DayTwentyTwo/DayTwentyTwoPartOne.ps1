$reboot_steps = Get-Content .\AdventCode\2021\DayTwentyTwo\day22_test_data.txt
$low_range = -50
$high_range = 50

$cubes = [System.Collections.ArrayList]@()
foreach($z_axis in $low_range..$high_range)
{
    $grid = [System.Collections.ArrayList]@()
    foreach($x_axis in $low_range..$high_range)
    {
        $line = [System.Collections.ArrayList]@()
        foreach($y_axis in $low_range..$high_range)
        {
            $line.Add(0) | Out-Null
        }
        $grid.Add($line) | Out-Null
    }
    $cubes.Add($grid) | Out-Null
}
$sum = 0
foreach($step in $reboot_steps)
{
    $action = IF ($step.Split()[0] -eq "on") {1} ELSE {0}
    $x_action = [System.ValueTuple[int, int]]::new($step.Split("=")[1].Replace(',y', '').Split('..')[0], $step.Split("=")[1].Replace(',y', '').Split('..')[2])
    $y_action = [System.ValueTuple[int, int]]::new($step.Split("=")[2].Replace(',z', '').Split('..')[0], $step.Split("=")[1].Replace(',y', '').Split('..')[2])
    $z_action = [System.ValueTuple[int, int]]::new($step.Split("=")[3].Split('..')[0], $step.Split("=")[3].Split('..')[2])

    $x_action.Item1 = IF ($x_action.Item1 -lt $low_range) {$low_range} ELSE {$x_action.Item1}
    $x_action.Item2 = IF ($x_action.Item2 -gt $high_range) {$high_range} ELSE {$x_action.Item2}
    $y_action.Item1 = IF ($y_action.Item1 -lt $low_range) {$low_range} ELSE {$y_action.Item1}
    $y_action.Item2 = IF ($y_action.Item2 -gt $high_range) {$high_range} ELSE {$y_action.Item2}
    $z_action.Item1 = IF ($z_action.Item1 -lt $low_range) {$low_range} ELSE {$z_action.Item1}
    $z_action.Item2 = IF ($z_action.Item2 -gt $high_range) {$high_range} ELSE {$z_action.Item2}

    for($k = $z_action.Item1; $k -le $z_action.Item2; $k++)
    {
        for($j = $y_action.Item1; $j -le $y_action.Item2; $j++)
        {
            for($i = $x_action.Item1; $i -le $x_action.Item2; $i++)
            {
                if($cubes[($k + [Math]::Abs($low_range))][($j + [Math]::Abs($low_range))][($i + [Math]::Abs($low_range))] -eq 0 -and $action -eq 1)
                {
                    $sum++
                }
                elseif($cubes[($k + [Math]::Abs($low_range))][($j + [Math]::Abs($low_range))][($i + [Math]::Abs($low_range))] -eq 1 -and $action -eq 0)
                {
                    $sum--
                }
                $cubes[($k + [Math]::Abs($low_range))][($j + [Math]::Abs($low_range))][($i + [Math]::Abs($low_range))] = $action
            }   
        }   
    }
}
$sum
$sum = 0
foreach($grid in $cubes)
{
    foreach($line in $grid)
    {
        $sum += ($line | Group-Object | Where-Object { $_.Name -eq 1}).Count
    }
}
$sum