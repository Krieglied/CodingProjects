function Get-LowPoints
{
    param(
        $vents
    )
    $max_col = $vents[0].Length - 1
    $max_row = $vents.Length - 1
    $low_points = @()
    for($i = 0; $i -lt ($max_row + 1); $i++)
    {
        for($j = 0; $j -lt ($max_col + 1); $j++)
        {
            if($i -eq 0 -and $j -eq 0)
            {
                if($vents[$i][$j] -lt $vents[0][1] -and $vents[$i][$j] -lt $vents[1][0])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($j -eq 0 -and $i -eq $max_row)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i][$j+1])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($j -eq $max_col -and $i -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i+1][$j])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($i -eq $max_row -and $j -eq $max_col)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i][$j-1])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($i -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i][$j+1] -and $vents[$i][$j] -lt $vents[$i+1][$j])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($j -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i+1][$j] -and $vents[$i][$j] -lt $vents[$i][$j+1])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($j -eq $max_col)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i+1][$j] -and $vents[$i][$j] -lt $vents[$i][$j-1])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            elseif($i -eq $max_row)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i][$j+1] -and $vents[$i][$j] -lt $vents[$i-1][$j])
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
            else {
                if(($vents[$i][$j] -lt $vents[$i][$j-1]) -and
                   ($vents[$i][$j] -lt $vents[$i][$j+1]) -and
                   ($vents[$i][$j] -lt $vents[$i+1][$j]) -and
                   ($vents[$i][$j] -lt $vents[$i-1][$j]))
                {
                    $low_points += [Convert]::ToInt32($vents[$i][$j]) - 48
                }
            }
        }
    }
    return $low_points
}

$vents = Get-Content .\day9_input_Graham.txt
$low_points = Get-LowPoints -vents $vents
$sum = 0
foreach($point in $low_points)
{
    $sum += $point + 1
}
$sum