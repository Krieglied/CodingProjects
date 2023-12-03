def build_list(line):
    temp_list = []
    list_line = list(line)
    list_line.pop(0)
    while len(list_line) > 0:
        value = list_line.pop(0)
        if value.isnumeric():
            temp_list.append(value)
        if value == '[':
            substring = value
            while value != ']':
                value = list_line.pop(0)
                substring += value
            temp_list.append(build_list(substring))
    return temp_list

def test_element(element1, element2):
    # If both elements are just integers
    if type(element1) != list and type(element2) != list:
        if element1 <= element2:
            return True
        return False
    # If both elements are list
    if type(element1) == list and type(element2) == list:
        while len(element1) > 0:
            if element1 != [] and element2 != []:
                new_element1 = element1.pop(0)
                new_element2 = element2.pop(0)
                total_test = test_element(new_element1, new_element2)
                if not total_test:
                    return False
                if len(element1) == 0 and total_test:
                    return True 
            elif element2 == []:
                return False
        return True
    # If one of them is a list and the other an integer
    if type(element1) == list and type(element2) != list:
        if element1 != []:
            if type(element1[0]) == list:
                return test_element(element1[0], element2)
            value1 = element1[0]
            if int(value1) <= int(element2):
                return True
        return False        
    # If one of them is a list and the other an integer
    if type(element2) == list and type(element1) != list:
        if element2 != []:
            if type(element2[0]) == list:
                return test_element(element1, element2[0])
            value2 = element2[0]
            if int(element1) <= int(value2):
                return True
        return False
        
    
data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

line_num = 0
index = 1
sum_indices = 0

while line_num < len(data):
    stack1 = build_list(data[line_num].replace(',', ''))
    line_num += 1
    stack2 = build_list(data[line_num].replace(',', ''))
    total_test = True
    while len(stack1) > 0 and len(stack2) > 0:
        element1 = stack1.pop(0)
        element2 = stack2.pop(0)
        total_test = test_element(element1, element2)
        if (len(stack1) == 0) or total_test:
            break
        if len(stack2) == 0 or not total_test:
            break
    if (len(stack1) == 0) and total_test or len(stack2) == 0:
        sum_indices += index
    line_num += 2
    print(f'Index {index} was in the {total_test} order.')
    index += 1

print(sum_indices)