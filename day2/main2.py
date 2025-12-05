"solves day 2 part 1"
import math

def main():
    
    with open("day2/input.txt", "r") as f:
        data = f.read().replace("\n", "")  # flatten
        parts = data.split(",")   

    invalid_ids = []
    for pair in parts:
            start, end = int(pair.split("-")[0]), int(pair.split("-")[1])
            for number in range(start, end + 1):
                str_num = str(number)
                firstpart, secondpart = str_num[:len(str_num)//2], str_num[len(str_num)//2:]
                if firstpart == secondpart:
                    invalid_ids.append(number)

            print(f"From {start} to {end}, found {len(invalid_ids)} invalid IDs: {invalid_ids}")
    
    result = math.fsum(invalid_ids)

    print(result)
if __name__ == '__main__':
    main()

