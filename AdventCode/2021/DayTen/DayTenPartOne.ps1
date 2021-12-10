$nav_commands = Get-Content .\day10_input_Graham.txt
$stack = [System.Collections.Stack]@()
$total_sum_errors = 0
$values = @{')'=3;']'=57;'}'=1197;'>'=25137}
$op_commands = @{'('=')';'['=']';'{'='}';'<'='>'}
foreach ($chunk in $nav_commands)
{
    foreach($command in $chunk.ToCharArray())
    {
        # If the character command is one of the beginning commands, add to the stack
        if($command -eq "(" -or $command -eq "[" -or $command -eq "{" -or $command -eq "<")
        {
            $stack.Push($command)
        }
        # If one of the end commands, test to see if last element of stack matches
        elseif($command -eq $op_commands[$stack.Peek().ToString()])
        {
            $null = $stack.Pop()
        }
        # Otherwise, the line is corrupted.  Start to compute the score
        else {
            $total_sum_errors += $values[$command.toString()]
            break
        }
    }
}
Write-Host "Total Sum of Errors :" $total_sum_errors
