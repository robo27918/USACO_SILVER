def least_greater_element(nums,target):
    '''
        returns the index of the least element greater than the target
    '''
    l,r =0, len(nums)-1
    while l<=r:
        mid  = (l + r)//2
        if nums[mid] <= target:
            l = mid +1
        else:
            r = mid -1
    return l
def main():
    # nums = [1,2,3,3,3,3,3]
    # print(last_occurence(nums,2))
    run_tests()
def run_tests():
  
    test_cases = [
        # target in middle, and greater element exists
        ([1, 3, 5, 7], 5, 3),
        
        # target matches last element
        ([1, 3, 5, 7], 7, 4),
        
        # target less than all elements
        ([10, 20, 30], 5, 0),

        # target greater than all elements
        ([1, 2, 3], 10, 3),

        # target between duplicates
        ([1, 2, 4, 4, 6], 4, 4),

        # duplicates: find strictly greater
        ([3, 3, 3, 4, 5], 3, 3),

        # all elements equal to target
        ([5, 5, 5], 5, 3),

        # empty list
        ([], 42, 0),

        # only one element and it's greater
        ([10], 5, 0),

        # only one element and it's not greater
        ([5], 5, 1),

        # multiple occurrences of greater element
        ([1, 2, 3, 6, 6, 6, 9], 4, 3),
    ]

    print("---least element greater than target test---")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = least_greater_element(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")


if __name__ =='__main__':
    main()