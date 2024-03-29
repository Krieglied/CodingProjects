function Build-NewPixel
{
    param(
        $pixels,
        $x,
        $y,
        $infinite_value
    )
    $enchanced_pixel = ""
    for($i = -1; $i -le 1; $i++)
    {
        for($j = -1; $j -le 1; $j++)
        {
            # If (x, y) is within pixels, then grab the current value
            # If not, then the value is 0
            if(($x + $j) -in 0..($pixels[0].Length - 1) -and ($y + $i) -in 0..($pixels.Count - 1))
            {
                $enchanced_pixel += $pixels[$y+$i][$x+$j]
            }
            else
            {
                $enchanced_pixel += $infinite_value
                
            }
        }
    }
    return $enchanced_pixel.Replace("#", "1").Replace(".", "0")
}
function Run-Algorithm
{
    param(
        $enchancement,
        $pixels,
        $infinite_value
    )
    $new_pixels = [System.Collections.ArrayList]@()
    for($y = -1; $y -lt ($pixels.Count + 1); $y++)
    {
        $pixel_line = ""
        for($x = -1; $x -lt ($pixels[0].Length + 1); $x++)
        {
            # After each pixel generates its image enhancement algorithm string,
            # make sure the string only consists of 0 and 1
            $enchanced_pixel = Build-NewPixel -pixels $pixels -x $x -y $y -infinite_value $infinite_value
            # After the line has been converted to a binary string, use the number
            # as an index of the enchancement string to see what new character is to
            # be added to the line
            $pixel_line += $enchancement[[Convert]::ToInt32($enchanced_pixel, 2)]
        }
        # All changed and new pixels for the line are added to the arraylist
        $new_pixels.Add($pixel_line) | Out-Null
    }
    return $new_pixels
}

$content = Get-Content .\AdventCode\2021\DayTwenty\day20_input_Graham.txt
$enchancement_alg = $content[0]
$pixels = [System.Collections.ArrayList]@()
$infinite_value = "."
# Generate the intital 2D-array
foreach($line in $content[2..($content.Length)])
{
    $pixel_line = [System.Collections.ArrayList]@()
    foreach($letter in $line)
    {
        $pixel_line.Add($letter) | Out-Null
    }
    $pixels.Add($letter) | Out-Null
}
# $i will control the numbers of steps to apply the enchancement algorithm
for($i = 0; $i -lt 2; $i++)
{
    $pixels = Run-Algorithm -pixels $pixels -enchancement $enchancement_alg -infinite_value $infinite_value
    $infinite_value = $enchancement_alg[([Convert]::ToInt32(($infinite_value.ToString()*9).Replace("#", "1").Replace(".", "0"), 2))]
}
$sum = 0
foreach($line in $pixels)
{
    $sum += [Regex]::Matches($line, "#").Count
}
$sum
