function New-ValuePacket
{
    param(
        $bit_string
    )
    $index = 0
    $value = ""
    $control = $bit_string[$index++]
    while($control -eq '1')
    {
        # The 4 bit after the control bit is added to the total value
        $value += $bit_string.Substring($index, 4)
        $index += 4
        $control = $bit_string[$index++]
    }
    $value += $bit_string.Substring($index, 4)
    $index += 4
    return [Convert]::ToInt32($value, 2), $index
}

function New-Packet{
    param(
        $bit_string,
        $has_length
    )
    $index = 0
    $version = [Convert]::ToInt32($bit_string.Substring($index, 3), 2)
    $index += 3
    $type_id = [Convert]::ToInt32($bit_string.Substring($index, 3), 2)
    $index += 3
    if($type_id -eq 4)
    {
        $value, $used_index = New-ValuePacket -bit_string $bit_string.Substring($index)
        $index += $used_index
    }
    else {
        $length_type_id = $bit_string[$index++]
        if($length_type_id -eq '0')
        {
            $length = [Convert]::ToInt32($bit_string.Substring($index, 15), 2)
            $index += 15
            $packet_lengths = 0
            while($length -gt $packet_lengths)
            {
                $packet_version, $used_index = New-Packet -bit_string $bit_string.Substring($index)
                $version += $packet_version
                $index += $used_index
                $packet_lengths += $used_index
            }            
        }
        else {
            $number_packets = [Convert]::ToInt32($bit_string.Substring($index, 11), 2)
            $index += 11
            #Write-Host "NUMBER OF PACKETS: " $number_packets
            for($i = 0; $i -lt $number_packets; $i++)
            {
                Write-Host "SUBSTRING LENGTH: " $bit_string.Length "INDEX: " $index
                $packet_version, $used_index = New-Packet -bit_string $bit_string.Substring($index) -has_length $True
                $version += $packet_version
                $index += $used_index
            }
        }
    }
    return $version, $index
}


$digits = Get-Content .\day16_input_Graham.txt
$hex_form = @{
    '0'= '0000'
    '1'= '0001'
    '2'= '0010'
    '3'= '0011'
    '4'= '0100'
    '5'= '0101'
    '6'= '0110'
    '7'= '0111'
    '8'= '1000'
    '9'= '1001'
    'A'= '1010'
    'B'= '1011'
    'C'= '1100'
    'D'= '1101'
    'E'= '1110'
    'F'= '1111'
}
$full_bit_string = ""
foreach($digit in $digits.ToCharArray())
{
    $full_bit_string += $hex_form[$digit.toString()]
}
#Write-Host "TOTAL LENGTH: " $full_bit_string.Length
New-Packet -bit_string $full_bit_string