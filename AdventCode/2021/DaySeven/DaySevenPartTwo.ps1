$crab_pos = Get-Content .\day7_input.txt
$crab_pos = $crab_pos.Split(',')
$mean = [int]($crab_pos | Measure-Object -Average).Average
$answer_sum = -1
$range = 10
$found = $False
$previous_sum = -1
while($found -eq $False)
{
    foreach($align in ($mean-$range)..($mean+$range))
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
    if($previous_sum -eq -1)
    {
        $previous_sum = $answer_sum
        $range += 10
        continue
    }
    if($previous_sum -eq $answer_sum)
    {
        $found = $True
    }
    $range += 10
}
$answer_sum
