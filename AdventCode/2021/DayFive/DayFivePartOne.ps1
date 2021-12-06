function New-StartingPoint
{
    param(
        $coord1,
        $coord2,
        $min
    )
    if($min -eq "x")
    {
        if([Math]::Min($coord1[0], $coord2[0]) -eq $coord1[0])
        {
            return $coord1, $coord2
        }
        return $coord2, $coord1
    }
    else 
    {
        if([Math]::Min($coord1[1], $coord2[1]) -eq $coord1[1])
        {
            return $coord1, $coord2
        }
        return $coord2, $coord1
    }
}


$field = @()
$row_size = $column_size = 9
foreach($i in 0..$row_size)
{
    $row = @()
    foreach($j in 0..$column_size)
    {
        $row += 0
    }
    $field += $row
}

$coords = Get-Content .\test_data.txt
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
        $coords = New-StartingPoint -coord1 ($x1, $y1) -coord2 ($x2, $y2) -min "x"
        $coords
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
