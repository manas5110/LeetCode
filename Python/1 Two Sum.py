class Computer:
    pass

c1 = Computer()
# print("Hello World")
print(id(c1))
nums = [2,3,4,5,6,7]
nums.insert(2,77)
nums.remove(77)
nums.pop()
del nums[3:]
nums.extend([13,14,15])
nums.sort(reverse=True)
print(nums)