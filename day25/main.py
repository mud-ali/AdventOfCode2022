import math

def isPowerFive(num):
    x = math.log(num, 5)
    return (x == int(x))

def mapping(num):
    if str(num) in "012": return int(num)
    elif str(num) == "=": return -2
    elif str(num) == "-": return -1

def snafuToDec(snafu):
    total = 0
    for i,digit in enumerate(snafu[::-1]):
        total += (5**i)*mapping(digit)
    return total

def decToSnafu(decNum):
    ans = ""
    decNumC = decNum
    while decNumC > 0:
        rem = decNumC % 5
        decNumC //= 5
        if rem <=2:
            ans = str(rem) + ans
        else:
            if rem == 3:
                ans = "="+ans
            elif rem == 4:
                ans = "-"+ans
            decNumC += 1
    return ans

def main():
    with open('input.txt','r') as file:
        data = file.read().split('\n')
        numsum = 0
        for line in data:
            numsum += snafuToDec(line)
        print(numsum) # 30638862852576
        print(decToSnafu(numsum))


if __name__ == '__main__':
    main()