def main():
    with open('input.txt', 'r') as file:
        elves = file.read().split('\n\n')
        mostCals = [0,0,0]
        for elf in elves:
            calories = 0
            for food in elf.split("\n"):
                calories += int(food)
            for cals in mostCals:
                if calories > cals:
                    replaceIndex = mostCals.index(min(mostCals))
                    
                    mostCals.pop(replaceIndex)
                    mostCals.insert(replaceIndex, calories)
                    break
        print(sum(mostCals))

if __name__ == '__main__':
    main()