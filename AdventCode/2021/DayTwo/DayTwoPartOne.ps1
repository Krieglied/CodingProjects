# Only notable comment about this problem, is using
# a switch made things pretty straightforward
$commands = Get-Content .\day2_input.txt
$horz_pos = 0
$depth = 0
foreach($command in $commands)
{
    switch($command.Split()[0])
    {
        'forward' { $horz_pos += [int]$command.Split()[1] }
        'up' { $depth -= [int]$command.Split()[1] }
        'down' { $depth += [int]$command.Split()[1] }
    }
}
$total = $depth * $horz_pos
$total
