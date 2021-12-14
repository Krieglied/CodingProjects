$polymers = Get-Content .\day14_input_Graham.txt
$poly_template = $polymers[0].ToCharArray()
$poly_pairs = @{}
$results = @{}
# The majority of letters to be used can be grabbed from the template
foreach($letter in $poly_template)
{
    if($results.Contains($letter) -ne $True)
    {
        $results[$letter] = 1
    }
    else {
        $results[$letter]++
    }
}
# Each insertion rule is added to a hashtable, with the rule itself
# as the key, and the letter to add and the times it needs to be run
# added as an Arraylist
foreach($line in $polymers[2..$polymers.Length])
{
    $components = $line.Split("->") | Where-Object {$_ -ne ""}
    $poly_pair = [System.Collections.ArrayList]@()
    $poly_pair.Add($components[1][1]) | Out-Null
    $poly_pair.Add(0) | Out-Null
    $poly_pairs.($components[0].Trim()) = $poly_pair
}
# This for loop initalizes the amount of each diagraph present
# within the template
for($i = 1; $i -lt $poly_template.Length; $i++)
{
    $poly_pairs[($poly_template[$i - 1] + $poly_template[$i])][1]++
}
$steps = 40
foreach($step in 1..$steps)
{
    # Only the diagraphs active at the start need to be processed
    # Also, the values at each diagraph needs to be recorded as well
    $active_keys = $poly_pairs.Keys | where-Object {$poly_pairs[$_][1] -ne 0}
    $active_values = [System.Collections.ArrayList]@()
    foreach($key in $active_keys)
    {
        $active_values.Add($poly_pairs[$key][1]) | Out-Null
    }
    $index = 0
    foreach($key in $active_keys)
    {
        # The current diagraph needs to have its number in the hashtable decreased
        # (we're removing them from the string) and the two digraphs created need 
        # to have their numbers increased (we're adding them to the string)
        $poly_pairs[$key][1] -= $active_values[$index]
        $poly_pairs[($key[0] + $poly_pairs[$key][0])][1] += $active_values[$index]
        $poly_pairs[($poly_pairs[$key][0] + $key[1])][1] += $active_values[$index]
        # The insertion rules might introduce new letters to the string
        # so they need to be added to results hashtable
        if($results.ContainsKey($poly_pairs[$key][0]) -ne $True)
        {
            $results[$poly_pairs[$key][0]] = $active_values[$index]
        }
        # We only need to count the middle letter of the trigraph multipled
        # by the number of times the diagraph got acted on
        else {
            $results[$poly_pairs[$key][0]] += $active_values[$index]
        }
        $index++
    }
}
$top = $0
$bottom = $null
# Simple search through the hashtable, finding the minimum and maximum counts
foreach($value in $results.Values)
{
    if($value -gt $top)
    {
        $top = $value
    }
    if($bottom -eq $null -or $value -lt $bottom)
    {
        $bottom = $value
    }
}
Write-Host "Max - Min: " ($top - $bottom)