# Grab all the numbers from the input file
$input = Get-Content -Path .\input.txt

# Iterate through each item in the number list
foreach ($item in $input) {

    #  Compute the difference between 2020 and the number being looked at
    $companion = 2020 - $item
    
    #  If the difference is also in the array
    if($input -contains $companion){
        #  Multiple the two captured number together and print the result
        $result = $companion * $item
        $result
        
        # End the loop
        break
    }
}
