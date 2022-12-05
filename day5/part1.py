#im lazy so i'm going to hard code the original stacks in as lists
def main():
    s = []
    with open('input.txt','r') as file:
        for i in range(9):
            s.append(list(file.readline().replace('\n','')))
        instructions = file.readlines()
        for cmd in instructions:
            cmdF = list(map(int, cmd.replace("move ",'').replace('\n','').replace(" from ",',').replace(" to ",",").split(",")))

            for i in range(cmdF[0]):
                s[cmdF[2]-1].append(s[cmdF[1]-1].pop())
    top = ''
    for stack in s:
        top += stack[-1]
    
    print(top)


if __name__ == '__main__':
    main()