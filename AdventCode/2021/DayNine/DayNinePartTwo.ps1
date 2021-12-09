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
                    $low_points += @($i, $j)
                }
            }
            elseif($j -eq 0 -and $i -eq $max_row)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i][$j+1])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($j -eq $max_col -and $i -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i+1][$j])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($i -eq $max_row -and $j -eq $max_col)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i][$j-1])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($i -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i][$j+1] -and $vents[$i][$j] -lt $vents[$i+1][$j])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($j -eq 0)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i+1][$j] -and $vents[$i][$j] -lt $vents[$i][$j+1])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($j -eq $max_col)
            {
                if($vents[$i][$j] -lt $vents[$i-1][$j] -and $vents[$i][$j] -lt $vents[$i+1][$j] -and $vents[$i][$j] -lt $vents[$i][$j-1])
                {
                    $low_points += @($i, $j)
                }
            }
            elseif($i -eq $max_row)
            {
                if($vents[$i][$j] -lt $vents[$i][$j-1] -and $vents[$i][$j] -lt $vents[$i][$j+1] -and $vents[$i][$j] -lt $vents[$i-1][$j])
                {
                    $low_points += @($i, $j)
                }
            }
            else {
                if(($vents[$i][$j] -lt $vents[$i][$j-1]) -and
                   ($vents[$i][$j] -lt $vents[$i][$j+1]) -and
                   ($vents[$i][$j] -lt $vents[$i+1][$j]) -and
                   ($vents[$i][$j] -lt $vents[$i-1][$j]))
                {
                    $low_points += @($i, $j)
                }
            }
        }
    }
    return $low_points
}

function Get-Neighbors
{
    param(
        $point
    )
    # Remember that [y][x] is x,y
    $neighbors = @()
    # Check to see if LEFT is a valid neighbor
    # If x-- >= 0
    if(($point[0] - 1) -ge 0)
    {
        $neighbors += ($point[0] - 1), $point[1]
    }
    # Check to see if UP is a valid neighbor
    # If y-- >= 0
    if(($point[1] - 1) -ge 0)
    {
        $neighbors += $point[0], ($point[1] - 1)
    }
    # Check to see if RIGHT is a valid neighbor
    # If x++ < row_length
    if(($point[1] + 1) -lt $global:vents[0].Length)
    {
        $neighbors += $point[0], ($point[1] + 1)
    }
    # Check to see if DOWN is a valid neighbor
    # If y++ < vents_length
    if(($point[0] + 1) -lt $global:vents.Length)
    {
        $neighbors += ($point[0] + 1), $point[1]
    }
    return $neighbors
}

function Get-BasinSize
{
    param(
        $point
    )
    $sum = 0
    # If space is 9, not a valid part of basin, return 0
    if($global:vents[$point[0]][$point[1]] -eq "9")
    {
        return $sum
    }
    for($i = 0; $i -lt $global:visited_spaces.Length; $i+=2)
    {
        # Check if point has already been visited, if so, return 0
        if($global:visited_spaces[$i] -eq ($point[0]) -and $global:visited_spaces[$i+1] -eq $point[1])
        {
            return $sum
        }
    }
    $global:visited_spaces += $point
    $neighbors = Get-Neighbors -point $point
    for($i = 0; $i -lt $neighbors.Length; $i+=2)
    {
        $sum += Get-BasinSize -point @($neighbors[$i], $neighbors[$i+1])
    }
    return $sum + 1
}


$global:vents = Get-Content .\day9_input_Graham.txt
$low_points = Get-LowPoints -vents $vents
$top_sums = 0, 0, 0
$sum = 0
for($i = 0; $i -lt $low_points.Length; $i += 2)
{
    $global:visited_spaces = @()
    $sum = Get-BasinSize -point @($low_points[$i], $low_points[$i+1])
    if($sum -gt $top_sums[0])
    {
        $top_sums[2] = $top_sums[1]
        $top_sums[1] = $top_sums[0]
        $top_sums[0] = $sum
    }
    elseif($sum -gt $top_sums[1])
    {
        $top_sums[2] = $top_sums[1]
        $top_sums[1] = $sum
    }
    elseif($sum -gt $top_sums[2])
    {
        $top_sums[2] = $sum
    }
}
$top_sums[0] * $top_sums[1] * $top_sums[2]