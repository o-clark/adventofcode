if __name__ == '__main__':
    letter_score = {x:ix+1 for ix, x in enumerate(map(chr, [*range(ord('a'), ord('z')+1), *range(ord('A'), ord('Z')+1)]))}
    with open('IO/d3.txt') as f_in:
        rucksacks = [l.strip('\n') for l in f_in]
        rucksack_sets = [set(r[:len(r)//2]).intersection(set(r[len(r)//2:])) for r in rucksacks]
        rucksack_scores = [list(map(letter_score.get, compartment)) for r in rucksack_sets for compartment in r]
        rucksack_total = sum([score for rucksack in rucksack_scores for score in rucksack])
        rucksack_groups = [rucksacks[i * 3:(i + 1) * 3] for i in range((len(rucksacks) + 3 - 1) // 3 )]
        group_badges = [set.intersection(*map(set, rg)) for rg in rucksack_groups]
        group_prio = sum(map(letter_score.get, [badge for group in group_badges for badge in group]))
        print(f"Total: {rucksack_total}, Priority Total: {group_prio}")