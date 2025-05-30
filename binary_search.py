def binary_search(nums,target):
    left = 0
    right = len(nums)-1

    while left<=right:
        
        mid = int((left + right )/2)
        print("mid is:",mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right =mid -1
        else:
            left = mid +1
    print(f"The number: {target} could not be found")
    return None


#index of first occurrence of target
def binary_search_first_occ(nums,target):
    left = 0
    right = len(nums)-1
    first_occ = None
    while left<=right:
        print("left & right",left, right)
        mid = int((left + right )/2)
        print("mid is:",mid)
        if nums[mid] == target:
            first_occ = mid
        
        if nums[mid] >= target:
            right =mid -1
            print(right)
        else:
            left = mid +1
    if first_occ != None:
        return first_occ
    print(f"The number: {target} could not be found")
    return None
#index of last occurence variant
def binary_search_last_occ(nums,target):
    left = 0
    right = len(nums)-1
    last_occ = None
    while left<=right:
        print("left & right",left, right)
        mid = int((left + right )/2)
        print("mid is:",mid)
        if nums[mid] == target:
            last_occ = mid
        
        if nums[mid] > target:
            right =mid -1
            print(right)
        elif nums[mid] <= target:
            left = mid +1
    if last_occ != None:
        return last_occ
    print(f"The number: {target} could not be found")
    return None
#index of least integer greater than target

'''
    in the case that the target is not in the array, what should we do?
        -

'''
def least_greater(nums,target):
    left = 0
    right = len(nums)
    while left<right:
        mid = (left + right)//2
      
        if nums[mid] <= target:
            left = mid +1
        else:
            right = mid
    return left

def modify_binary_search(nums,target):
    '''
        return the index of target,or the index where it should be at
        if not present in the nums array
    '''
    left = 0
    right = len(nums) -1

    while left <right:

        mid =(left + right)//2
       
        if nums[mid] == target: 
            return mid
        if nums[mid]<=target:
            left = mid + 1
        elif nums[mid]> target:
            right = mid -1
    return left

nums = [1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4]
nums2 = [5,5,5,5,5]
nums3 = [1,2,3,5]
nums4 = [1,2,4,5]
nums5 = [1,2,3,3,3,5,6]
print("@ index position:",modify_binary_search(nums5,2))
idx1= least_greater(nums5,3)
print("the index of least element is greater than target is",idx1, "with value", nums5[idx1])

def run_tests():
    test_cases = [
        ([1, 3, 5, 7, 9], 5, 3),
        ([1, 3, 5, 7, 9], 6, 3),
        ([1, 3, 5], 10, 3),
        ([2, 4, 6], 0, 0),
        ([5, 5, 5], 5, 3),
        ([1, 2, 4, 6, 6, 7, 8], 5, 3),
        ([], 5, 0),
        ([1, 3, 5, 5, 5, 6, 7], 5, 5),
        ([2, 4, 6, 8], 8, 4),
        ([2, 4, 6, 8], 2, 1),
    ]
    print("---left binary search test")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = least_greater(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")

    print("\n---right binary search test---")

run_tests()

