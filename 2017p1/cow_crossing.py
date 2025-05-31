def read_input(file):
    '''
        returns the nums list and the range of queries
    '''
    lines = [line.strip('\n') for line in open(file,'r')]
    C,N = lines[0].split()
    C,N= int(C), int(N)
    T= []
    for i in  range(1,C+1):
        T.append(int(lines[i]))
    AB =[]
    for j in range(C+1,len(lines)):
        line = lines[j].split()
        AB.append((int(line[0]),int(line[1])))

    print(T)
    print(AB)

def main():
    print("from main..")
    read_input('2017p1\helpcross.in')
if __name__=="__main__":
    main()