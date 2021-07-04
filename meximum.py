def numbers(nums):
    i=0
    max=0
    while i<len(nums):
        if nums[i]>max:
            max=nums[i]
        i=i+1
    print(max)
numbers(nums=[3,5,7,34,2,89,2,5])            
        