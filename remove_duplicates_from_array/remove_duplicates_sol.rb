# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    if nums.length > 2
        i = 0
        while i < nums.length-1
            if nums[i] == nums[i+1]
                nums.delete_at(i+1)
            else
                i += 1
            end
        end
    elsif nums.length == 2
        if nums[0] == nums[1]
            nums.delete_at(0)
        end
    else
        nums
    end
    nums.length
end
