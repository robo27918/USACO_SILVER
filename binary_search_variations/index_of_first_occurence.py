def first_occurrence(nums,target):
    '''
        returns the index of the first occurence of the target
        assuming nums is sorted

    '''
    l,r = 0,len(nums)-1
    while l<=r:
        mid = (l + r)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] >= target:
            r= mid-1
    return l
def run_tests():
    test_cases = [
        # target appears once
        ([1, 3, 5, 7, 9], 5, 2),

        # target appears multiple times
        ([1, 2, 4, 4, 4, 5, 6], 4, 2),

        # target at beginning
        ([3, 3, 4, 5, 6], 3, 0),

        # target at end
        ([1, 2, 3, 5, 5], 5, 3),

        # target smaller than all elements
        ([2, 3, 4, 5], 1, 0),

        # target greater than all elements
        ([1, 3, 5, 7], 10, 4),

        # target not present, would go in middle
        ([1, 3, 5, 7], 4, 2),

        # empty array
        ([], 1, 0),

        # all elements same and equal to target
        ([2, 2, 2, 2], 2, 0),

        # all elements same but target not present
        ([2, 2, 2, 2], 3, 4),

        # single element match
        ([5], 5, 0),

        # single element no match
        ([4], 5, 1),
    ]

    print("---left binary search test (first occurrence or insertion point)")
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = first_occurrence(nums, target)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"
    print("All tests passed!")

def main():
    # nums1 = [1,2,2,1,1,1,3,4,5] # show how to sort
    # nums1 = sorted(nums1) #O(n * log(n))
    # print(nums1)
    # print(first_occurrence(2,nums1))
    run_tests()

if __name__ =="__main__":
    main()