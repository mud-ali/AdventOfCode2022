def main():
    with open('input.txt','r') as file:
        games = file.read().split('\n')
        totalScore = 0
        for game in games:
            score = 0
            elf, me = game.split()
            match me:
                case 'Y':
                    score += 3
                    me = elf
                case 'Z':
                    score += 6
                    # i feel like there was a better way then brute forcing the permutations of this but its
                    # small enough that it works
                    me = 'B' if elf == 'A' else ('A' if elf =='C' else 'C')
                case 'X':
                    me = 'C' if elf == 'A' else ('B' if elf =='C' else 'A')
            score += (ord(me)-64)

            totalScore += score
        print(totalScore)


if __name__ == '__main__':
    main()