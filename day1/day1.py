with open('input.txt', 'r+') as file:
    fileText = file.read()
filedata = fileText.split('\n')
numbers = [ int(x) for x in filedata ]
target_num = 2020

#part 1
# for i, num in enumerate(numbers[:-1]): 
#     complementary = target_num - num
#     if complementary in numbers[i+1:]: 
#         print("Nums: {} and {}, product: {}".format(num, complementary, num * complementary))

#part 2
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)
 
i = subset_sum(numbers,2020)
print(list(i)) #[[305, 264, 54, 51, 1346], [483, 565, 972], [51, 1969]]

print(483 * 565 * 972)

