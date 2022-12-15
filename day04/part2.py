def main():
    with open('input.txt','r') as file:
        elf_pairs = file.read().splitlines()
        count = 0
        for pair in elf_pairs:
            elf1, elf2 = pair.split(",")
            oneStart, oneEnd = list(map(int, elf1.split("-")))
            twoStart, twoEnd = list(map(int, elf2.split("-")))
            if (twoStart >= oneStart and twoStart <= oneEnd) or (oneStart >= twoStart and oneStart <= twoEnd):
                count += 1
        print(count)


if __name__ == '__main__':
    main()