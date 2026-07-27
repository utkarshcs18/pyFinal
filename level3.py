#1
nums = [2, 4, 6, 18, 4, 2, 10]
unique = []
remove = []

for i in nums:
    if i not in unique:
        unique.append(i)
    else:
        remove.append(i)

print(nums)
print(unique)
print(remove)

max  = nums[0] 
min = nums[0]

for i in nums:
    if i > max:
        max = i

    if i < min:
        min = i

print(max)
print(min)



    


#4
lists = [x for x in range (1, 101) if x % 2 == 0 and x % 7 == 0]
print(lists)