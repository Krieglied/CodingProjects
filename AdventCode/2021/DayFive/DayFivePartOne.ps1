$field = @()
$row_size = $column_size = 999
foreach($i in 0..$row_size)
{
    $row = @()
    foreach($j in 0..$column_size)
    {
        $row += 0
    }
    $field += $row
}

$coords = Get-Content .\day5_input.txt
$coords = $coords.replace('->', ' ')
$coords = $coords.Split('  ') | Where-Object {$_ -ne ''}

for($i = 0; $i -lt ($coords.Length); $i+=2)
{
    $x1 = [int]$coords[$i].Split(',')[0]
    $y1 = [int]$coords[$i].Split(',')[1]
    $x2 = [int]$coords[$i+1].Split(',')[0]
    $y2 = [int]$coords[$i+1].Split(',')[1]
    if($x1 -eq $x2)
    {
        $index = $x1
        for($j = [Math]::Min($y1, $y2); $j -le [Math]::Max($y1, $y2); $j++)
        {
            $field[$j*($row_size+1)+$index]++
        }
    }
    elseif($y1 -eq $y2)
    {
        $row = $y1
        for($j = [Math]::Min($x1, $x2); $j -le [Math]::Max($x1, $x2); $j++)
        {
            $field[$row*($row_size+1)+$j]++
        } 
    }
    else
    {
        if($x2 -gt $x1 -and $y2 -gt $y1)
        {
            for(; $x1 -le $x2 -and $y1 -le $y2; $x1++, $y1++)
            {
                $field[$y1*($row_size + 1) + $x1]++
            }
        }
        elseif ($x1 -gt $x2 -and $y1 -gt $y2) 
        {
            for(; $x2 -le $x1 -and $y2 -le $y1; $x2++, $y2++)
            {
                $field[$y2*($row_size + 1) + $x2]++
            }    
        }
        elseif ($x1 -gt $x2 -and $y2 -gt $y1) 
        {
            for(; $x1 -ge $x2 -and $y1 -le $y2; $x1--, $y1++)
            {
                $field[$y1*($row_size + 1) + $x1]++
            }    
        }
        elseif ($x2 -gt $x1 -and $y1 -gt $y2) 
        {
            for(; $x2 -ge $x1 -and $y2 -le $y1; $x2--, $y2++)
            {
                $field[$y2*($row_size + 1) + $x2]++
            }
        }
    }
}
$sum = 0
foreach($element in $field)
{
    if($element -ne 0 -and $element -ne 1)
    {
        $sum++
    }
}
$sum
