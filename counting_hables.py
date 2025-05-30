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
    idx = -1
    while l <=r:
        mid = (l+r)//2
        if nums[mid]<target:
            l = mid +1
        elif nums[mid] >= target:
            r = mid -1
        # else:
        #     return mid
    
    return l

def r_binary_search(nums,target):
    '''
        returns the index where target should be inserted at the end, or the index of the last occurence
    '''
    if not nums:
        return 0
    
    l = 0
    r = len(nums)-1
    while l <=r:
        mid = (l + r)//2
        if nums[mid]<=target:
            l = mid +1
        elif nums[mid] > target:
            r = mid-1
   
    if nums[r] == target:
        return r
    return l

def main():
    # nums,ranges =read_input("haybales.in")

    # #for loop to go thru all the queries
    # with open("haybales.out",'w') as file:
    #     for range in ranges:
    #         file.write(str(count_nums_in_range(nums,range)) +"\n")
    # file.close()
    # run_tests()
  

def run_tests():
    test_cases = [
        # x exists in the list
    ([1, 3, 3, 5, 7], 3, 1),
    
    # x is smaller than all elements
    ([10, 20, 30], 5, 0),
    
    # x is larger than all elements
    ([1, 2, 3], 10, 3),
    
    # x would go in the middle
    ([1, 2, 4, 5], 3, 2),
    
    # empty list
    ([], 42, 0),
    
    # all elements equal to x
    ([5, 5, 5, 5], 5, 0),
    
    # duplicates, x not in list
    ([1, 2, 4, 4, 6], 3, 2),
    
    # another valid test
    ([1, 3, 5, 7, 9], 4, 2),
    
    # x less than all duplicates
    ([3, 3, 3, 3], 2, 0),
    
    # x greater than all duplicates
    ([3, 3, 3, 3], 4, 4),
        

    ]

    r_test_cases = [
        # target exists multiple times, return last occurrence
        ([1, 3, 3, 3, 5, 7, 8], 3, 3),

        # target exists once
        ([1, 3, 5, 7, 9], 5, 2),

        # target would be inserted in the middle
        ([1, 3, 5, 7, 9], 4, 2),

        # target less than all elements
        ([10, 20, 30], 5, 0),

        # target greater than all elements
        ([1, 2, 3], 10, 3),

        # empty list
        ([], 42, 0),

        # all elements equal to target
        ([5, 5, 5, 5], 5, 3),

        # all elements equal but target is different
        ([5, 5, 5, 5], 6, 4),
        ([5, 5, 5, 5], 4, 0),

        # target between duplicates
        ([1, 2, 4, 4, 6], 3, 2),

        # target not in list, should go between
        ([1, 2, 4, 4, 6], 5, 4),
    ]
    print("---left binary search test")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = l_binary_search(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")
    print("\n---right binary search test")
    for i, (nums, target, expected) in enumerate(r_test_cases, 1):
        result = r_binary_search(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")       

if __name__ == "__main__":
    main()