def read_input(file):
    '''
        returns the nums list and the range of queries
    '''
    lines = [line.strip('\n') for line in open(file,'r')]
    n,q = lines[0].split()
    n,q= int(n), int(q)
    print(lines[1])
    #convert nums to numerical values for comparison
    nums = [int(num) for num in lines[1].split()]
    #sort nums for use in binary search
    nums.sort()# O(n*lg(n)) cost
    #build the queries
    ranges=[]
    for line in lines[2:]:
        r =  line.split()
        ranges.append((int(r[0]), int (r[1])))
    return nums,ranges
            


def count_nums_in_range(nums,range):
    #TODO: implement binary search to count
    # the occurence of each number within the range
    lower,upper = range[0],range[1]
    

 

def main():
    nums,ranges =read_input("counting_hables.txt")
    
    

if __name__ == "__main__":
    main()