$commands = Get-Content .\day2_input.txt
$horz_pos = 0
$depth = 0
foreach($command in $commands)
{
    if($command.Split()[0] -eq 'forward')
    {
        $horz_pos += [int]$command.Split()[1]
    }
    if($command.Split()[0] -eq 'up')
    {
        $depth -= [int]$command.Split()[1]
    }
    if($command.Split()[0] -eq 'down')
    {
        $depth += [int]$command.Split()[1]
    }
}
$total = $depth * $horz_pos
$total