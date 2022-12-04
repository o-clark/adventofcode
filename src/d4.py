with open('IO/d4.txt', 'r') as f_in:
    elf_pairs = [l.strip('\n').split(',') for l in f_in]
    elf_sets = [set(range(int(section.split('-')[0]), int(section.split('-')[1]) + 1)) for elf in elf_pairs for section in elf]
    elf_sets_pairs = [elf_sets[i:i + 2] for i in range(0, len(elf_sets), 2)]
    elf_overlap = sum([not(pair[0] - pair[1]) or not(pair[1] - pair[0]) for pair in elf_sets_pairs])
    any_elf_overlap =  sum([bool(pair[0].intersection(pair[1])) for pair in elf_sets_pairs])
    print(f"P1: {elf_overlap}, P2: {any_elf_overlap}")