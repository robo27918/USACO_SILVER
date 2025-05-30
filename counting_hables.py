def read_input(file):
    '''
        returns the nums list and the range of queries
    '''
    lines = [line.strip('\n') for line in open(file,'r')]
    n,q = lines[0].split()
    n,q= int(n), int(q)
   
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
            


def count_nums_in_range(nums,query_range):
    '''
        1.turn nums into set for quick look up
        2. create a counter varible to track how many of the numbers in the range are actually in
            nums list
        3. iterate thru the range to do a check if i
    '''
    nums = set(nums)
    counter = 0
    l,u = query_range[0],query_range[1]
    for n in range(l,u+1):
        if n in nums:
            counter +=1
    return counter
def l_binary_search(nums,target):
    '''
        returns the index where x should be inserted, or the index of the first occurence
    '''
    l = 0
    r = len(nums)-1
    while l <=r:
        mid = (l+r)//2
        if nums[mid]<target:
            pass
        elif nums[mid] > target:
            pass
        else:
            return mid
    return l


 

def main():
    nums,ranges =read_input("haybales.in")

    #for loop to go thru all the queries
    with open("haybales.out",'w') as file:
        for range in ranges:
            file.write(str(count_nums_in_range(nums,range)) +"\n")
    file.close()
        

if __name__ == "__main__":
    main()