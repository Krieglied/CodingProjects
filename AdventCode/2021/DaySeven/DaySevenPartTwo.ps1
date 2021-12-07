$crab_pos = Get-Content .\day7_input.txt
$crab_pos = $crab_pos.Split(',')
$max_pos = $crab_pos | Measure-Object -Maximum
$answer_sum = -1
foreach($align in 0..$max_pos.Maximum)
{
    $current_sum = 0
    foreach($crab in $crab_pos)
    {
        $distance = [Math]::Abs([int]$crab - $align)
        # Part 2 introduces adding the sum of numbers, with n
        # equal to the distance between the starting position
        # and the new alignment
        $current_sum += ($distance*($distance + 1)) / 2
    }
    if($answer_sum -eq -1)
    {
        $answer_sum = $current_sum
        continue
    }
    if($current_sum -lt $answer_sum)
    {
        $answer_sum = $current_sum
    }
}
$answer_sum