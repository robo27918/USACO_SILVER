def last_occurence(nums,target):
    '''
        returns the index of the last occurence of an element
        or returns the index where it should be inserted if not in the list
    '''
    l,r =0, len(nums)-1
    while l<=r:
        mid  = (l + r)//2
        if nums[mid] <= target:
            l = mid +1
        else:
            r = mid -1
    if 0<=l-1<=len(nums)-1 and nums[l-1] == target:
        return l-1
    return l
def main():
    # nums = [1,2,3,3,3,3,3]
    # print(last_occurence(nums,2))
    run_tests()
def run_tests():
    test_cases = [
        # target appears once
        ([1, 3, 5, 7, 9], 5, 2),

        # target appears multiple times
        ([1, 2, 4, 4, 4, 5, 6], 4, 4),

        # target at beginning
        ([3, 3, 4, 5, 6], 3, 1),

        # target at end
        ([1, 2, 3, 5, 5], 5, 4),

        # target smaller than all elements
        ([2, 3, 4, 5], 1, 0),

        # target greater than all elements
        ([1, 3, 5, 7], 10, 4),

        # target not present, would go in middle
        ([1, 3, 5, 7], 4, 2),

        # empty array
        ([], 1, 0),

        # all elements same and equal to target
        ([2, 2, 2, 2], 2, 3),

        # all elements same but target not present
        ([2, 2, 2, 2], 3, 4),

        # single element match
        ([5], 5, 0),

        # single element no match
        ([4], 5, 1),
    ]

    print("---right binary search test (last occurrence or insertion point)")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = last_occurence(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")

if __name__ =='__main__':
    main()