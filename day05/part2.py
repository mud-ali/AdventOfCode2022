def main():
    s = []
    with open('input.txt','r') as file:
        for i in range(9):
            s.append(list(file.readline().replace('\n','')))
        instructions = file.readlines()
        for cmd in instructions:
            amt, start, to = list(map(int, cmd.replace("move ",'').replace('\n','').replace(" from ",',').replace(" to ",",").split(",")))
            start -=1
            to -= 1
            if amt > 1:
                s[to] += s[start][-amt:]
                s[start] = s[start][:len(s[start])-amt]
            else:
                s[to].append(s[start].pop())

    # get the top of every stack
    top = ''
    for stack in s:
        top += stack[-1]
    
    print(top)


if __name__ == '__main__':
    main()