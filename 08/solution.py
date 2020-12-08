def load_instructions(filename):
    operations = []
    arguments = []
    with open(filename) as f:
        for line in f:
            split_line = line.split()
            operations.append(split_line[0])
            arguments.append(split_line[1])

    return operations, arguments


def process_operations(operations, arguments):
    accumulator = 0
    counter = 0
    instruction_tracker = []
    prev_accumulator = 0
    while True:

        if counter in instruction_tracker:
            break
        else:
            instruction_tracker.append(counter)

        instruction = operations[counter]
        argument = arguments[counter]

        prev_accumulator = accumulator

        if instruction == "acc":
            accumulator += int(argument)
            print(instruction, argument, accumulator, counter)
            counter += 1
            continue
        elif instruction == "jmp":
            counter += int(argument)
            print(instruction, argument, accumulator, counter)
            continue
        elif instruction == "nop":
            print(instruction, argument, accumulator, counter)
            counter += 1
            continue

    print(prev_accumulator)


def process_operations_part_2(operations, arguments):
    accumulator = 0
    counter = 0
    instruction_tracker = []
    prev_accumulator = 0
    while counter <= len(operations) - 1:

        if counter in instruction_tracker:
            print("Loop Detected")
            return False
        else:
            instruction_tracker.append(counter)

        instruction = operations[counter]
        argument = arguments[counter]

        # Used to return value for Part #1
        prev_accumulator = accumulator

        if instruction == "acc":
            accumulator += int(argument)
            # print(instruction, argument, accumulator, counter)
            counter += 1
            continue
        elif instruction == "jmp":
            counter += int(argument)
            # print(instruction, argument, accumulator, counter)
            continue
        elif instruction == "nop":
            # print(instruction, argument, accumulator, counter)
            counter += 1
            continue

    print(f"accumulator: {accumulator}")
    return True


def alter_operation(operations, arguments):
    idx = 0
    while True:
        copy_of_operations = operations.copy()
        op = copy_of_operations[idx]
        if op == "nop":
            copy_of_operations[idx] = "jmp"
            if process_operations_part_2(copy_of_operations, arguments):
                break

        elif op == "jmp":
            copy_of_operations[idx] = "nop"
            if process_operations_part_2(copy_of_operations, arguments):
                break

        idx += 1


ops, args = load_instructions("input.txt")
# process_operations_part_2(ops, args)
alter_operation(ops, args)
