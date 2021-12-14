$polymers = Get-Content .\day14_input_Graham.txt
$poly_template = [System.Collections.ArrayList]@()
$poly_pairs = [System.Collections.ArrayList]@()
# The inital polymer template is stored
foreach($polymer in $polymers[0].ToCharArray())
{
    $poly_template.Add($polymer) | Out-Null
}
# Each of the pair insertion rules is stored within a tuple
# (the string pair to find, char to insert)
foreach($line in $polymers[2..$polymers.Length])
{
    $results = $line.Split("->") | Where-Object {$_ -ne ""}
    $poly_pairs.Add([System.Tuple[string, string]]::new($results[0], $results[1])) | Out-Null
}
$steps = 10
foreach($step in 1..$steps)
{
    $insertion_pairs = [System.Collections.ArrayList]@()
    for($i = 1; $i -lt $poly_template.Count; $i++)
    {
        foreach($pair in $poly_pairs)
        {
            # Once the appropriate rule is found, add the transformation and index to the tuple
            if($pair.item1 -match ($poly_template[$i - 1] + $poly_template[$i]))
            {
                $insertion_pairs.Add([System.Tuple[char, int]]::new($pair.Item2[1], $i)) | Out-Null
                break
            }
        }
    }
    # Start inserting from the back of the template
    $insertion_pairs = $insertion_pairs | Sort-Object -Property Item2 -Descending
    foreach($insert in $insertion_pairs)
    {
        $poly_template.Insert($insert.Item2, $insert.Item1)
    }
}
$charCount = @()
# Count the number of occurences for each unique letter in the template
foreach($letter in ($poly_template | Select-Object -Unique))
{
    $charCount += [System.Tuple[int, char]]::new(($poly_template | Where-Object {$_ -eq $letter} | Measure-Object).Count, $letter)
}
$charCount = $charCount | Sort-Object -Property Item1
Write-Host "Max - Min: " ($charCount[$charCount.Count - 1].Item1 - $charCount[0].Item1)