$crab_pos = Get-Content .\day7_input.txt
$crab_pos = $crab_pos.Split(',')
$max_pos = $crab_pos | Measure-Object -Maximum
$answer_sum = -1
foreach($align in 0..$max_pos.Maximum)
{
    $current_sum = 0
    foreach($crab in $crab_pos)
    {
        $current_sum += [Math]::Abs([int]$crab - $align)
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