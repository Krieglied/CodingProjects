# Only real difference between Part One and Part Two
# is the forward comment introduced two actions, instead of one

$commands = Get-Content .\day2_input.txt
$horz_pos = 0
$depth = 0
$aim = 0
foreach($command in $commands)
{
    switch($command.Split()[0])
    {
        'forward' 
        { 
            $horz_pos += [int]$command.Split()[1]
            $depth += $aim * [int]$command.Split()[1] 
        }
        'up' { $aim -= [int]$command.Split()[1] }
        'down' { $aim += [int]$command.Split()[1] }
    }
}
$total = $depth * $horz_pos
$total
