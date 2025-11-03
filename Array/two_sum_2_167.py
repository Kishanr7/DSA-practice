def twoSum(numbers, target):
    while len(numbers):
        z = numbers.pop()
        if target-z in numbers:
            return [numbers.index(target-z)+1, len(numbers)+ 1]
        
print(twoSum([2,7,11,15],9))