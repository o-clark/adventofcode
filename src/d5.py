with open('IO/d5.txt', 'r') as f_in:
    stack_text, instructions = f_in.read().split('\n\n')
    stacks = list(map(list, zip(*[[line[i:i+4].strip().replace('[', '').replace(']', '') for i in range(0, len(line), 4)] for line in stack_text.split('\n')]))) #split, chunk into 4, transpose
    clean_stacks,clean_stacks_p2 = [list(filter(bool, stack)) for stack in stacks], [list(filter(bool, stack)) for stack in stacks] #remove empty strings
    for instruction in instructions.strip('\n').split('\n'):
        amount, from_stack, to_stack = filter(bool, [int(word) if all(c.isdigit() for c in word) else '' for word in instruction.split()]) #split instructions into 3 integers
        clean_stacks_p2[to_stack - 1] = clean_stacks_p2[from_stack -1 ][:amount] + clean_stacks_p2[to_stack - 1] #shift n blocks over
        clean_stacks_p2[from_stack -1] = clean_stacks_p2[from_stack -1][amount:] #remove blocks
        for i in range(0, amount):
            clean_stacks[to_stack - 1].insert(0, clean_stacks[from_stack - 1].pop(0)) #Shift one block at a time
    print(f'{"".join([s[0] for s in clean_stacks])}, {"".join([s[0] for s in clean_stacks_p2])}')