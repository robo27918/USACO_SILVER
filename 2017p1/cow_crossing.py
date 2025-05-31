def read_input(file):
    '''
        returns the chicken times in sorted order, and the time range the
        chickens are available
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
    return sorted(T),AB
def solve(T,AB):
    '''
        Brute Force: loop thru T and check if they 

        returns: the maximum # of cow-chicken pairs that can be constructed
    '''
    count = 0
    used = set()
    for t in T:
        for l,u in AB:
            # print(t)
            # print(l,u)
            if t in range(l,u+1) and (l,u) not in used:
                used.add((l,u))
                count +=1
                break

    return count
def main():
    print("from main..")
    T,AB =read_input('2017p1\helpcross.in')
    print(solve(T,AB))
    
if __name__=="__main__":
    main()