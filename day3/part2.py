def get_priorities(letters_list):
    priorities = []
    for letter in letters_list:
        if letter == letter.lower():
            priorities.append(ord(letter) - 96)
        elif letter == letter.upper():
            priorities.append(ord(letter) - 38)
    return priorities

def main():
    with open('input.txt', 'r') as file:
        rucksacks = file.read().split('\n')
        groups = []
        i=0
        while len(groups) < len(rucksacks)/3:
            group = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
            groups.append(group)
            i+=3

        dupes = []
        for group in groups:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    dupes.append(item)
                    break

        prioritySum = sum(get_priorities(dupes))
        print(prioritySum)

if __name__ == '__main__':
    main()