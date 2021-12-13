$dots = Get-Content .\day13_input_Graham.txt
$collection_of_dots = @()
$instructions = @()
foreach($dot in $dots)
{
    # For most of the lines, values are stored into a value tuple as (x, y)
    # Use of the valueTuple is so that the coordinates can be changed later
    if($dot[0] -ne "f" -and $dot -ne "")
    { 
        $collection_of_dots += [System.ValueTuple[int, int]]::new([int]$dot.split(',')[0], [int]$dot.split(',')[1])
    }
    # For the instruction lines, a normal tuple can be used to stored over which direction to fold
    elseif($dot[0] -eq "f")
    {
        $instructions += [System.Tuple[string, int]]::new($dot.split('=')[0][-1], [int]$dot.split('=')[1])
    }
}
# Importantly, part 2 needs to run through all instructions
foreach($inst in $instructions)
{
    $x = If($inst.Item1 -eq "x") { $inst.Item2 } Else {0}
    $y = If($inst.Item1 -eq "y") { $inst.Item2 } Else {0}
    for($i = 0; $i -lt $collection_of_dots.Count; $i++)
    {
        # If $y != 0, then we fold along the y-axis.  If the point
        # is before the fold, no need to change the value.  If not,
        # new value is ($y * 2 - y_pos)
        if($y -ne 0 -and $collection_of_dots[$i].Item2 -gt $y)
        {
            $collection_of_dots[$i].Item2 = ($y*2 - $collection_of_dots[$i].Item2)
        }
        # If $x != 0, then we fold along the x-axis.  If the point
        # is before the fold, no need to change the value.  If not,
        # new value is ($x * 2 - x_pos)
        if($x -ne 0 -and $collection_of_dots[$i].Item1 -gt $x)
        {
            $collection_of_dots[$i].Item1 = ($x*2 - $collection_of_dots[$i].Item1)
        }
    }
}
$max_row = ($collection_of_dots | Measure-Object -Property Item2 -Maximum).Maximum
$max_col = ($collection_of_dots | Measure-Object -Property Item1 -Maximum).Maximum
# Printer for the letters
for($y = 0; $y -le $max_row; $y++)
{
    $line = ""
    for($x = 0; $x -le $max_col; $x++)
    {
        if($collection_of_dots.Contains([System.ValueTuple[int, int]]::new($x, $y)))
        {
            $line += "#"
        }
        else {
            $line += "."
        }
    }
    $line
}