nums = [25, 12, 36, 95, 14]

print(nums[2])

names = ['john', 'doe', 'mary', 'jane']

print(names)

values  = [9.5, 'Toto', 25]

print(values)

mil = [nums, names]

print(mil)
"""Append to list"""

nums.append(45)

print(nums)

nums.pop()
print(nums)


del nums[2:]

print(nums)

nums.extend([29, 12, 13, 46])

print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))