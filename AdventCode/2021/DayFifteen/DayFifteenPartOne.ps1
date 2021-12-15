function Get-Neighbors
{
    param(
        $grid,
        $point
    )
    # Remember that [y][x] is x,y
    $neighbors = @()
    # Check to see if LEFT is a valid neighbor
    # If x-- >= 0
    if(($point[0] - 1) -ge 0)
    {
        $node = [Node]::new()
        $node.Point = [System.Tuple[int, int]]::new(($point[0] - 1), $point[1])
        $node.Weight = $grid[($point[0] - 1)][$point[1]]
        $node.Neighbors = $False 
        $neighbors += $node
    }
    # Check to see if UP is a valid neighbor
    # If y-- >= 0
    if(($point[1] - 1) -ge 0)
    {
        $node = [Node]::new()
        $node.Point = [System.Tuple[int, int]]::new($point[0], ($point[1] - 1))
        $node.Weight = $grid[$point[0]][($point[1] - 1)]
        $node.Neighbors = $False
        $neighbors += $node
    }
    # Check to see if RIGHT is a valid neighbor
    # If x++ < row_length
    if(($point[1] + 1) -lt $grid[0].Count)
    {
        $node = [Node]::new()
        $node.Point = [System.Tuple[int, int]]::new($point[0], ($point[1] + 1))
        $node.Weight = $grid[$point[0]][($point[1] + 1)]
        $node.Neighbors = $False
        $neighbors += $node
    }
    # Check to see if DOWN is a valid neighbor
    # If y++ < vents_length
    if(($point[0] + 1) -lt $grid.Count)
    {
        $node = [Node]::new()
        $node.Point = [System.Tuple[int, int]]::new(($point[0] + 1), $point[1])
        $node.Weight = $grid[($point[0] + 1)][$point[1]]
        $node.Neighbors = $False
        $neighbors += $node
    }
    return $neighbors
}


class Node{
    [System.Tuple[int, int]]$Point
    [int]$Weight
    [object[]]$Neighbors
}

function Get-Dijkstra
{
    param(
        $graph        
    )
    $source = $graph[0]
    $target = $graph[$graph.Count - 1]
    $list_of_nodes = [System.Collections.ArrayList]@()
    $sdistance = @{}
    $previous = @{}

    foreach($vertex in $graph)
    {
        $sdistance[$vertex.Point] = [int]::MaxValue
        $previous[$vertex.Point] = $null
        $list_of_nodes.Add($vertex) | Out-Null
    }
    $sdistance[$source.Point] = 0
    $nearest_node = $null

    while($list_of_nodes.Count -gt 0)
    {
        $shortest_distance = [int]::MaxValue
        foreach($vertex in $list_of_nodes)
        {
            if($sdistance[$vertex.Point] -lt $shortest_distance)
            {
                $shortest_distance = $sdistance[$vertex.Point]
                $nearest_node = $vertex
            }
        }
        $list_of_nodes.Remove($nearest_node)

        if($nearest_node -eq $target)
        {
            Write-Host "Shortest Distance: " $shortest_distance
        }


        foreach($neighbor in $nearest_node.Neighbors)
        {
            $alt = $shortest_distance + $neighbor.Weight
            if($alt -lt $sdistance[$neighbor.Point])
            {
                $sdistance[$neighbor.Point] = $alt
                $previous[$neighbor.Point] = $nearest_node
            }
        }
    }
}



$input_values = Get-Content .\day15_input_Graham.txt
$nodes = [System.Collections.ArrayList]@()
foreach($line in $input_values)
{
    $node_line = [System.Collections.ArrayList]@()
    foreach($letter in $line.TocharArray())
    {
        $node_line.Add([int]$letter - 48) | Out-Null
    }
    $nodes.Add($node_line) | Out-Null
}
$new_nodes = [System.Collections.ArrayList]@()

for($y = 0; $y -lt $nodes.Count; $y++)
{
    for($x = 0; $x -lt $nodes[$y].Count; $x++)
    {
        $node = [Node]::new()
        $node.Point = [System.Tuple[int, int]]::new($x, $y)
        $node.Weight = $nodes[$y][$x]
        $node.Neighbors = (Get-Neighbors -grid $nodes -point ($x, $y))
        $new_nodes.Add($node) | Out-Null
    }
}
Get-Dijkstra -graph $new_nodes