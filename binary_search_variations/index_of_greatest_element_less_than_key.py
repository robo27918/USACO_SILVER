def least_greater_element(nums,target):
    '''
        returns the index of the greatest element less than the key
    '''
    l,r =0, len(nums)-1
    while l<=r:
        mid  = (l + r)//2
        if nums[mid] < target:
            l = mid +1
        else:
            r = mid -1
    return l-1
def main():
    # nums = [1,2,3,3,3,3,3]
    # print(last_occurence(nums,2))
    run_tests()
def run_tests():
  
    test_cases = [
        # target in middle, and smaller element exists
        ([1, 3, 5, 7], 5, 1),  # 3 is the greatest < 5
        
        # target matches first element
        ([1, 3, 5, 7], 1, -1),  # nothing less than 1

        # target greater than all
        ([10, 20, 30], 40, 2),  # 30 is greatest < 40

        # target less than all
        ([10, 20, 30], 5, -1),

        # duplicates: target in between duplicates
        ([1, 2, 4, 4, 6], 4, 1),  # 2 is the greatest < 4

        # all elements equal to target
        ([5, 5, 5], 5, -1),

        # all elements less than target
        ([1, 2, 3], 5, 2),

        # all elements greater than target
        ([6, 7, 8], 5, -1),

        # target between duplicates
        ([1, 1, 1, 2, 2, 3], 2, 2),

        # empty list
        ([], 42, -1),

        # only one element, and it's less
        ([3], 5, 0),

        # only one element, and it's not less
        ([5], 5, -1),
    ]

    print("---greatest element less than target test---")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = least_greater_element(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")



if __name__ =='__main__':
    main()