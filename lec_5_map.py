def sashadaun(a):
    return (a%3 == 0)

nums = [34, 45, 67, 69, 74]
result = list(map(sashadaun, nums))

print(result)



def my_func(a, b):
    return a*b
 
nums1 = [6, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 5]
 
nums_multiply = list(map(my_func, nums1, nums2))
 
print(nums_multiply)