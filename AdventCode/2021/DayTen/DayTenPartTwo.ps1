$nav_commands = Get-Content .\day10_input_Graham.txt
$incomplete_lines = [System.Collections.ArrayList]@()
$op_commands = @{'('=')';'['=']';'{'='}';'<'='>'}
foreach ($chunk in $nav_commands)
{
    # This time if the line is corrupted, skip over it
    $corrupted = $False
    $stack = [System.Collections.Stack]@()
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
        # Otherwise, the line is corrupted.  Set the flag variable and don't add the symbols to
        # the Arraylist
        else {
            $corrupted = $True
            break
        }
        
    }
    # If the line is simply incomplete, add the stack object to the Arraylist
    if($corrupted -eq $False)
    {
        $incomplete_lines.Add($stack) | Out-Null
    }
    
}
$completion_scores = [System.Collections.ArrayList]@()
$values = @{'('=1;'['=2;'{'=3;'<'=4}
foreach($line in $incomplete_lines)
{
    $total_complete_sum = 0
    while($line.Count -gt 0)
    {
        # Since each set of incomplete lines is simply a stack, pop the element
        # and perform the computation per character
        $total_complete_sum *= 5
        $total_complete_sum += $values[$line.Pop().toString()]
    }
    $completion_scores.Add($total_complete_sum) | Out-Null
}
$completion_scores = $completion_scores | Sort-Object -Property $number
Write-Host "Middle Completion Score :" $completion_scores[$completion_scores.Count / 2]
