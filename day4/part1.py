def main():
    with open('test.txt','r') as file:
        elf_pairs = file.read().splitlines()
        count = 0
        for pair in elf_pairs:
            elf1, elf2 = pair.split(",")
            oneStart, oneEnd = list(map(int, elf1.split("-")))
            twoStart, twoEnd = list(map(int, elf2.split("-")))
            if (oneStart >= twoStart and oneEnd<=twoEnd) or (twoStart >= oneStart and twoEnd <= oneEnd):
                count += 1
        print(count)


if __name__ == '__main__':
    main()