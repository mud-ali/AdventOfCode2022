import sys

def checkCurrentFourteen(currentFourteen, index):
    if len(currentFourteen) < 14: return False
    for each in currentFourteen:
        if currentFourteen.count(each) > 1:
            return False
    print(index)
    sys.exit(0)
    

def main():
    with open('input.txt','r') as file:
        dataStream = file.readline().replace("\n",'')
        currentFourteen = []
        for i,signal in enumerate(dataStream):
            checkCurrentFourteen(currentFourteen, i)
            if len(currentFourteen) == 14: currentFourteen.pop(0)
            currentFourteen.append(signal)
            
if __name__ == '__main__':
    main()