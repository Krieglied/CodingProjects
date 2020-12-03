# Since the slopes are going to be analyzed with slightly different numbers
# better to run this as a function
function TreeCount{
    param (
        $slope,
        $counter
    )
    $input = Get-Content -Path .\input3.txt
    $start = 0
    # Using slope 2 for the down 2 requirement
    if($slope -ne 2)
    {
        foreach($item in $input){
            # Since the grid provided repeats, the input doesn't really need to be modified
            # Just restart the coordinates if the value goes past the end of the string
            if($start -ge $item.Length)
            {
                $start = $start - $item.Length
            }
            # We hit a tree! Increment counter
            if($item[$start] -eq '#')
            {
                $counter = $counter + 1
            }
            # For the first 4 slopes, since the function is provided the angle of slope
            # add it to the counter here
            $start = $start + $slope
        }
        $counter
    }
    else
    {
        # A line counter will be used to check track of the y-axis
        $line = 0
        foreach($item in $input){
            # Jump if the line is odd
            if($line % $slope -ne 0)
            {
                $line = $line + 1
                continue
            }
            # Since the grid provided repeats, the input doesn't really need to be modified
            # Just restart the coordinates if the value goes past the end of the string
            if($start -ge $item.Length)
            {
                $start = $start - $item.Length
            }
            # We hit a tree! Increment counter
            if($item[$start] -eq '#')
            {
                $counter = $counter + 1
            }
            $start = $start + 1
            $line = $line + 1
        }
        $counter
    }
}


# Use an array to store the values and then multiply them together
$slopeValues = 0,0,0,0,0
$slopeValues[0] = TreeCount -slope 1 -counter $slopeValues[0] -input $input
$slopeValues[1] = TreeCount -slope 3 -counter $slopeValues[1] -input $input
$slopeValues[2] = TreeCount -slope 5 -counter $slopeValues[2] -input $input
$slopeValues[3] = TreeCount -slope 7 -counter $slopeValues[3] -input $input
$slopeValues[4] = TreeCount -slope 2 -counter $slopeValues[4] -input $input
$slopeValues[0] * $slopeValues[1] * $slopeValues[2] * $slopeValues[3] * $slopeValues[4]
