def main():
    with open('input.txt', 'r') as file:
        elves = file.read().split('\n\n')
        mostCals = 0
        for elf in elves:
            calories = 0
            for food in elf.split("\n"):
                calories += int(food)
            if calories > mostCals:
                mostCals = calories
        print(mostCals)

if __name__ == '__main__':
    main()