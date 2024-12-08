with open('input.txt') as file_object:
    data = file_object.readlines()

def combine_terms(op1, operator, op2):
    if isinstance(op1, list):
        return op1 + [operator, op2]
    else:
        return [op1, operator, op2]

operators = ["+", "*", "||"]
true_equations_total = 0

for line in data:
    pieces = line.strip().split(":")
    total_value = int(pieces[0])
    operands = pieces[1].split()
    expressions = []
    for index in range(len(operands) - 1):
        if not expressions:
            expressions.append(combine_terms(operands[index], operators[0], operands[index + 1]))
            expressions.append(combine_terms(operands[index], operators[1], operands[index + 1]))
        else:
            tmp_list = []
            for oplist in expressions:
                tmp_list.append(combine_terms(oplist, operators[0], operands[index + 1]))
                tmp_list.append(combine_terms(oplist, operators[1], operands[index + 1]))
            expressions.clear()
            expressions.extend(tmp_list)

    for exp in expressions:
        while len(exp) > 1:
            op1 = exp.pop(0)
            op2 = exp.pop(0)
            op3 = exp.pop(0)
            if op2 == "+":
                exp.insert(0, int(op1) + int(op3))
            else:
                exp.insert(0, int(op1) * int(op3))
    expressions = set([item[0] for item in expressions])
    for exp in expressions:
        if int(exp) == total_value:
            true_equations_total += total_value
            break

print(f"TOTAL CALIBRATION RESULT: {true_equations_total}")

true_equations_total = 0

for line in data:
    pieces = line.strip().split(":")
    total_value = int(pieces[0])
    operands = pieces[1].split()
    expressions = []
    for index in range(len(operands) - 1):
        if not expressions:
            expressions.append(combine_terms(operands[index], operators[0], operands[index + 1]))
            expressions.append(combine_terms(operands[index], operators[1], operands[index + 1]))
            expressions.append(combine_terms(operands[index], operators[2], operands[index + 1]))
        else:
            tmp_list = []
            for oplist in expressions:
                tmp_list.append(combine_terms(oplist, operators[0], operands[index + 1]))
                tmp_list.append(combine_terms(oplist, operators[1], operands[index + 1]))
                tmp_list.append(combine_terms(oplist, operators[2], operands[index + 1]))
            expressions.clear()
            expressions.extend(tmp_list)

    for exp in expressions:
        while len(exp) > 1:
            op1 = exp.pop(0)
            op2 = exp.pop(0)
            op3 = exp.pop(0)
            if op2 == "+":
                exp.insert(0, str(int(op1) + int(op3)))
            elif op2 == "*":
                exp.insert(0, str(int(op1) * int(op3)))
            elif op2 == "||":
                exp.insert(0, op1 + op3)
    expressions = set([item[0] for item in expressions])
    for exp in expressions:
        if int(exp) == total_value:
            true_equations_total += total_value
            break

print(f"TOTAL MOD CALIBRATION RESULT: {true_equations_total}")