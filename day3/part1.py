def main():
    with open('input.txt', 'r') as file:
        rucksacks = file.read().split('\n')
        dupes = []
        for sack in rucksacks:
            halfPoint = int(len(sack)/2)
            comp1 = set(sack[0:halfPoint:1])
            comp2 = set(sack[halfPoint :len(sack) :1])

            for item in comp1:
                if item in comp2:
                    dupes.append(item)
                    print(item)
        
        priorities = []
        for dupe in dupes:
            if dupe == dupe.lower():
                priorities.append(ord(dupe) - 96)
            elif dupe == dupe.upper():
                priorities.append(ord(dupe) - 38)
        
        print(sum(priorities))

if __name__ == '__main__':
    main()