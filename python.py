# def count_occurrences(arr, n, x):
#     count = 0
#     for i in range(n):
#         if arr[i] == x:
#             count += 1
#     return count
# n = int(input("Enter the number of inputs: "))
# arr = [int(x) for x in input("Enter the array elements separated by space: ").split()]
# n = len(arr)
# x=int(input("Enter the number to be occurance"))
# print(count_occurrences(arr, n, x))
x=int(input("Enter the size of the array"))
a = [int(x) for x in input("Enter the array elements separated by space: ").split()]
for i in range(x):
    if a[i]==x:
        count+=1
        
    print(count)