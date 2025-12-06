import math

def main():

    with open("day3/input.txt", "r") as f:
        data = f.read()
        banks = data.split("\n")   
    joltages = []
    for bank in banks:
        left = 0
        right = 0
        position = 0
        for i in range (len(bank) - 1):
            number = int(bank[i])
            if number > left:
                left = number
                position = bank.index(bank[i])
                
        for i in range(position + 1, len(bank)):
            number = int(bank[i])
            if number > right:
                right = number
        print(f"the Joltage for bank {bank} is {int(str(left) + str(right))}")
        joltages.append(int(str(left) + str(right)))

    print(f"the total of output is {math.fsum(joltages)}")
if __name__ == '__main__':
    main()

