import sys

def checkCurrentFour(currentFour, index):
    if len(currentFour) < 4: return False
    for each in currentFour:
        if currentFour.count(each) > 1:
            return False
    print(index)
    sys.exit(0)
    

def main():
    with open('input.txt','r') as file:
        dataStream = file.readline().replace("\n",'')
        currentFour = []
        for i,signal in enumerate(dataStream):
            checkCurrentFour(currentFour, i)
            if len(currentFour) == 4: currentFour.pop(0)
            currentFour.append(signal)
            
if __name__ == '__main__':
    main()