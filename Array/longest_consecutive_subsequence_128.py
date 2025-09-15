# Algorithm Explanation:
# Problem: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Approach:
# 1. Convert the array to a set for O(1) lookups.
# 2. Iterate through each number in the set:
#    - If the number is the start of a sequence (num - 1 not in set), begin counting.
#    - Continue to check for consecutive numbers (num + 1, num + 2, ...) and count the streak.
#    - Update the longest streak found.
# 3. Return the length of the longest consecutive sequence.

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    return longest_streak
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([1,0,1,2]))