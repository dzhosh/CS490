import numpy as np

nums = np.random.random_integers(0,20,15)
print(nums)

print(np.argmax(np.bincount(nums)))

nums.sort()
count = 0
max_count = 0
best = -1
previous = -1
for num in nums:
    if num == previous:
        count += 1
    else:
        if count > max_count:
            max_count = count
            best = previous
        count = 1
        previous = num
print("Most frequent number is ", best, ", with a frequency of ", max_count, ".")
