def read_data(file_path):
    with open(file_path, 'r') as file:
        ranges = []
        ids = []
        has_seen_blank = False
        for line in file:
            if not has_seen_blank:
                has_seen_blank = line.strip() == ''
                if has_seen_blank:
                    continue
                low, high = line.strip().split('-')
                ranges.append((int(low), int(high)))
            else:
                ids.append(int(line.strip()))
            
    return ranges, ids

def main():
    ranges, ids = read_data("day5/input.txt")

    fresh_ids = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                fresh_ids += 1
                break
    print(f"There are {fresh_ids} fresh IDs.")
if __name__ == '__main__':
    main()