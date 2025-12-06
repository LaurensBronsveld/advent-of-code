import math

def main():

    with open("day3/input.txt", "r") as f:
        data = f.read()
        banks = data.split("\n")   
    joltages = []
    digits = 12
    for bank in banks:
        batteries = []
        position = -1
        counter = digits
        for i in range(digits):
            counter -= 1
            value = 0
            for i in range (position + 1,  len(bank) - counter):
                number = int(bank[i])
                if number > value:
                    value = number
                    position = i
            batteries.append(value)

        print(f"the Joltage for bank {bank} is {int(''.join(map(str, batteries)))}")
        joltages.append(int(''.join(map(str, batteries))))

    print(f"the total of output is {math.fsum(joltages)}")
if __name__ == '__main__':
    main()
