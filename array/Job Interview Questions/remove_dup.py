nums = [0,0,1,1,1,2,2,3,3,4,5,5]
def remove_duplicates_from__sorted_array(nums):
    a_ptr = 0
    b_ptr = 1
    while(b_ptr < len(nums)):
        if nums[a_ptr] != nums[b_ptr]:
            a_ptr+=1
            nums[a_ptr] = nums[b_ptr]
        b_ptr+=1
    return nums

n = remove_duplicates_from__sorted_array(nums)

print(n)
