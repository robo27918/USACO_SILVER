def read_input(file):
    lines = [line.strip('\n') for line in open(file,'r')]
    n,q = lines[0].split()
    n,q= int(n), int(q)
    print(lines[1])
    #convert nums to numerical values for comparison
    nums = [int(num) for num in lines[1].split()]
    #sort nums for use in binary search
    


 

def main():
    read_input("counting_hables.txt")

if __name__ == "__main__":
    main()