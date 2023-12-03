function Move-Pod
{
    param(
        $hallway,
        $siderooms
    )
    foreach($space in $hallway)
    {
        if($space.Value -ne "0" -and $space.moved )
    }
}

class Node
{
    [string]$Value
    [bool]$moved
}


$amphipod = Get-Content .\AdventCode\2021\DayTwentyThree\day23_input_Graham.txt
$hallway = [System.Collections.ArrayList]@()
for($i = 0; $i -lt 7; $i++)
{
    $node = [Node]::new()
    $node.moved = $false
    $node.Value = "0"
    $hallway.Add($node) | Out-Null
}
$siderooms = [System.Collections.ArrayList]@()
foreach($line in $amphipod[2..5])
{
    $sideroom = [System.Collections.Stack]@()
    $column = $line.Split("#") | Where-Object {$_ -ne ""}
    foreach($item in $column)
    {
        $node = [Node]::new()
        $node.moved = $false
        $node.Value = $item
        $sideroom.Push($Node)
    }
    $siderooms.Add($sideroom) | Out-Null
}