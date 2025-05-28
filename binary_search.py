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
nums = [1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4]
print("@ index position:",binary_search_first_occ(nums,4))
