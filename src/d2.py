if __name__ == '__main__':
    with open('IO/d2.txt','r') as f_in:
        points_1_map = {'A X':4,'A Y':8,'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6}
        points_2_map = {'A X':3,'A Y':4,'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7}
        points_1, points_2 = [],[]
        for line in f_in:
            line = line.strip('\n')
            points_1.append(points_1_map[line])
            points_2.append(points_2_map[line])
        total_points, total_points_2 = sum(points_1), sum(points_2)
        print(f"P1: {total_points}, P2: {total_points_2}")