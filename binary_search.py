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
    pass

def modify_binary_search(nums,target):
    '''
        return the index of target,or the index where it should be at
        if not present in the nums array
    '''
    left = 0
    right = len(nums) -1

    while left <=right:

        mid =(left + right)//2
       
        if nums[mid] == target: 
            return mid
        elif nums[mid]<target:
            left = mid + 1
        elif nums[mid]> target:
            right = mid -1
    return left

nums = [1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4]
nums2 = [5,5,5,5,5]
nums3 = [1,2,3,5]
nums4 = [1,2,4,5]
nums5 = [1,3,5,6]
print("@ index position:",modify_binary_search(nums5,2))
