# Pretty straightforward this problem
# Making sure each item is an int, compare the current line
# to the previous.  If greater, add one to the sum
# If the lines are not cast to int first, then
# the comparsion 9xx and 10xx will make the sum
# off by one
$layers = Get-Content .\day1_input.txt
$counter = 0
$previous = $layers[0]
foreach ($layer in $layers)
{
    if([int]$layer -gt [int]$previous)
    {
        $counter++
    }
    $previous = $layer
}
$counter
