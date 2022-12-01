$target_box = (Get-Content .\day17_input_Graham.txt).Split("=")
$lower_x = [int]$target_box[1].Split("..")[0]
$upper_x = [int]$target_box[1].Split("..")[2].Split(",")[0]
$lower_y = [int]$target_box.Split("=")[2].Split("..")[0]
$upper_y = [int]$target_box.Split("=")[2].Split("..")[2]
$maximum_height = 0
for($x = 0; $x -lt [Math]::Abs($lower_y); $x++)
{
    for($y = 0; $y -lt [Math]::Abs($lower_y); $y++)
    {
        $velocity_x = $x
        $velocity_y = $y
        $coord = [System.ValueTuple[int,int]]::new(0,0)
        $max_height = 0
        while(($coord.Item2 -gt $lower_y) -and ($coord.Item1 -lt $upper_x))
        {
            $coord.Item1 += $velocity_x
            $coord.Item2 += $velocity_y
            # If low_x <= x <= high_x and low_y <= y <= highy_Y
            if(($lower_x -le $coord.Item1 -and $coord.Item1 -le $upper_x) -and
            ($lower_y -le $coord.Item2 -and $coord.Item2 -le $upper_y))
            {
                if($max_height -gt $maximum_height)
                {
                    $maximum_height = $max_height
                }
                break
            }
            if($velocity_x -gt 0)
            {
                $velocity_x--
            }
            elseif($x -lt 0)
            {
                $velocity_x++
            }
            $velocity_y--
            if($velocity_y -eq 0)
            {
                $max_height = $coord.Item2
            }
        }
    }
}
Write-Host "MAX HEIGHT IS: " $maximum_height