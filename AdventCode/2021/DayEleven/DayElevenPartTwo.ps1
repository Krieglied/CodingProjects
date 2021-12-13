function Edit-Neighbors
{
    param(
        $x,
        $y,
        $grid
    )
    # Check to see if LEFT of current space has any valid neighbors
    # If x-- >= 0
    if(($x - 1) -ge 0)
    {
        $grid[$y][$x - 1] += 1
        # Checking the Diagonal neighbor above
        if(($y - 1) -ge 0)
        {
            $grid[$y - 1][$x - 1] += 1
        }
        # Checking the Diagonal neighbor below
        if(($y + 1) -lt $grid.Count)
        {
            $grid[$y + 1][$x - 1] += 1
        }
    }
    # Check to see if UP is a valid neighbor
    # If y-- >= 0
    if(($y - 1) -ge 0)
    {
        $grid[$y - 1][$x] += 1
    }
    # Check to see if RIGHT is a valid neighbor
    # If x++ < row_length
    if(($x + 1) -lt $grid[0].Count)
    {
        $grid[$y][$x + 1] += 1
        # Checking the Diagonal neighbor above
        if(($y - 1) -ge 0)
        {
            $grid[$y - 1][$x + 1] += 1
        }
        # Checking the Diagonal neighbor below
        if(($y + 1) -lt $grid.Count)
        {
            $grid[$y + 1][$x + 1] += 1
        }
    }
    # Check to see if DOWN is a valid neighbor
    # If y++ < vents_length
    if(($y + 1) -lt $grid.Count)
    {
        $grid[$y + 1][$x] += 1
    }
}


$octopi = Get-Content .\AdventCode\2021\DayEleven\day11_input_Graham.txt
$grid = [System.Collections.ArrayList]@()
$total_flashes = 0
foreach($octo_line in $octopi)
{
    $line = [System.Collections.ArrayList]@()
    foreach($number in $octo_line.ToCharArray())
    {
        $line.Add(([int]$number - 48)) | Out-Null
    }
    $grid.Add($line) | Out-Null
}
$step = 1000
foreach($number in 1..$step)
{
    
    $flash_coords = [System.Collections.ArrayList]@()
    for($y = 0; $y -lt $grid.Count; $y++)
    {
        for($x = 0; $x -lt $grid[$y].Count; $x++)
        {
            $grid[$y][$x] += 1
        }
    }
    $done_flashing = $False
    while($done_flashing -ne $True)
    {
        $done_flashing = $True
        for($y = 0; $y -lt $grid.Count; $y++)
        {
            for($x = 0; $x -lt $grid[$y].Count; $x++)
            {
                if($grid[$y][$x] -gt 9 -and (New-Object 'Tuple[int, int]' $x, $y) -notin $flash_coords)
                {
                    $done_flashing = $False
                    $total_flashes += 1
                    $flash_coords.Add((New-Object 'Tuple[int, int]' $x, $y)) | Out-Null
                    Edit-Neighbors -x $x -y $y -grid $grid
                }
            }
        }
    }
    foreach($coord in $flash_coords)
    {
        $grid[$coord.Item2][$coord.Item1] = 0
    }
    if($flash_coords.Count -eq 100)
    {
        Write-Host $number
        break
    }
}