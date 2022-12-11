def next_pixel(clock_cycle, current_pos):
    pos = (clock_cycle - 1) % 40
    if pos in [(current_pos - 1), current_pos, (current_pos + 1)]:
        return '#'
    return '.'

data = []

with open('./data.txt') as file_object:
    data = file_object.readlines()

record_signal = [20, 60, 100, 140, 180, 220]
signal_sum = 0
current_signal = 1
clock_cycle = 1

crt_string = []

for line in data:
    if line.strip() == 'noop':
        if clock_cycle == 41 or (clock_cycle > 42 and clock_cycle % 40 - 1 == 0):
            crt_string.append('\n')
        crt_string.append(next_pixel(clock_cycle, current_signal))
        clock_cycle += 1
    else:
        if clock_cycle == 41 or (clock_cycle > 42 and clock_cycle % 40 - 1 == 0):
            crt_string.append('\n')
        crt_string.append(next_pixel(clock_cycle, current_signal))
        clock_cycle += 1
        if clock_cycle == 41 or (clock_cycle > 42 and clock_cycle % 40 - 1 == 0):
            crt_string.append('\n')
        crt_string.append(next_pixel(clock_cycle, current_signal))
        if clock_cycle in record_signal:
            signal_sum += (clock_cycle * current_signal)
        current_signal += int(line.strip().split(' ')[1])
        clock_cycle += 1

    if clock_cycle in record_signal:
        signal_sum += (clock_cycle * current_signal)
        

print(signal_sum)
print(''.join(crt_string))