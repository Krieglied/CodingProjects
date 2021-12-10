$nav_commands = Get-Content .\day10_input_Graham.txt
$stack = [System.Collections.Stack]@()
$total_sum_errors = 0
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
        elseif(($command -eq ")" -and $stack.Peek() -eq "(") -or 
            ($command -eq "]" -and $stack.Peek() -eq "[") -or 
            ($command -eq "}" -and $stack.Peek() -eq "{") -or 
            ($command -eq ">" -and $stack.Peek() -eq "<"))
        {
            $null = $stack.Pop()
        }
        # Otherwise, the line is corrupted.  Start to compute the score
        else {
            if($command -eq ")")
            {
                $total_sum_errors += 3
            }
            if($command -eq "]")
            {
                $total_sum_errors += 57
            }
            if($command -eq "}")
            {
                $total_sum_errors += 1197
            }
            if($command -eq ">")
            {
                $total_sum_errors += 25137
            }
            break
        }
    }
}
$total_sum_errors