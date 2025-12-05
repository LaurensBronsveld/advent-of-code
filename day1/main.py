class Dial:
    position: int
    counter: int

    def __init__(self, position):
        self.position = position
        self.counter = 0

    def turn_left(self, steps):
        if self.position == 0:
            self.counter -= 1
        self.position = (self.position - steps)
        if self.position <= 0:
            rotations = abs(self.position) // 100
            self.counter += rotations + 1
            temp = str(self.position)[-2:]
            if temp.__contains__("-"):
                temp = temp.replace("-", "")
            self.position = 100 - int(temp)

    def turn_right(self, steps):
        self.position = (self.position + steps)
        if self.position > 99:
            rotations = self.position // 100
            self.counter += rotations
            self.position = int(str(self.position)[-2:])

        

    def check_position(self):
        if self.position == 100:
            self.position = 0
        print(f"the current position is: {self.position}")


def main():
    test_input = ["L1068",
        "L30",
        "R148",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"]
    
    f = open("day1/input.txt", "r")
    input = f.read().splitlines()       

    dial = Dial(50)

    for line in input:
        direction = line[0]
        steps = int(line[1:])

        if direction == "L":
            dial.turn_left(steps)
        elif direction == "R":
            dial.turn_right(steps)
        
        dial.check_position()

    print(f"The password is: {dial.counter}")


if __name__ == '__main__':
    main()

