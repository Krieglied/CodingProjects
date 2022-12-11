data = []

with open('./data.txt') as file_object:
    data = file_object.readlines()

record_signal = [20, 60, 100, 140, 180, 220]
signal_sum = 0
current_signal = 1
clock_cycle = 1

for line in data:
    if line.strip() == 'noop':
        clock_cycle += 1
    else:
        clock_cycle += 1
        if clock_cycle in record_signal:
            signal_sum += (clock_cycle * current_signal)
        current_signal += int(line.strip().split(' ')[1])
        clock_cycle += 1

    if clock_cycle in record_signal:
        signal_sum += (clock_cycle * current_signal)
        

print(signal_sum)