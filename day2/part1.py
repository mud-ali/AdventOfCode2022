def main():
    with open('input.txt','r') as file:
        games = file.read().split('\n')
        totalScore = 0
        for game in games:
            score = 0
            elf, me = game.split()
            me = chr(ord(me)-23)
            score += (ord(me)-64)
            if me == elf:
                score += 3
            # manual checking of all win scenarios - i dont enjoy efficiency
            elif (me == 'B' and elf == 'A') or (me == 'A' and elf == 'C') or (me == 'C' and elf == 'B'):
                score += 6
            totalScore += score
        print(totalScore)


if __name__ == '__main__':
    main()