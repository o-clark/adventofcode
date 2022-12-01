def find_calories(elves):
    calories_per_elf = [sum([int(calorie) for calorie in e.split('\n')]) for e in elves]
    top_calorie = max(calories_per_elf)
    top_3 = sum(sorted(calories_per_elf)[-3:])
    return top_calorie,top_3
    
if __name__ == '__main__':
    with open('IO/d1.txt','r') as f_in:
        elves = f_in.read()[:-1].split('\n\n')
        top_calorie,top_3 = find_calories(elves)
        print(f"Top Calories: {top_calorie}, Top 3: {top_3}")
