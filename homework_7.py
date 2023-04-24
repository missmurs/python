
'''
Write a Python program to compute the difference between two lists.

Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']

Expected Output:

first-second: ['a', 'b']

second-first: ['e']
'''
def compute_difference(first: list, second: list) -> tuple:

    set1 = set(first)
    set2 = set(second)


    diff_first_second = list(set1 - set2)


    diff_second_first = list(set2 - set1)

    return (diff_first_second, diff_second_first)



first_list = ['a', 'b', 'c', 'd']
second_list = ['c', 'd', 'e']


diff = compute_difference(first_list, second_list)

print("first-second:", diff[0])
print("second-first:", diff[1])

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6

Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6

Output: [0,1]
'''


def sum_of_two(nums: list, target: int) -> list:

    nums_dict = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_dict:
            return [i, nums_dict[diff]]
        nums_dict[num] = i
    return []
'''
Write a program that takes a list of integers as input and returns a new list that contains only the elements that are 
unique (i.e., that appear only once in the list). For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output 
list should be [1, 3, 4]. You can not use set data structure. It`s also forbidden to use the count method.
'''
def find_unique_elements(lst):
    unique_lst = []
    for i in lst:
        if lst.count(i) == 1:
            unique_lst.append(i)
    return unique_lst

'''
Write a program that takes a list of integers as input and returns a new list that contains only the elements that 
appear an odd number of times in the list. For example, if the input list is [1, 2, 3, 2, 4, 5, 5], the output list 
should be [1, 3, 4].
'''
def find_odd_occurrences(lst):
    unique_lst = set(lst)
    odd_occurrences = []
    for i in unique_lst:
        if lst.count(i) % 2 != 0:
            odd_occurrences.append(i)
    return odd_occurrences
'''
Write a program that takes a list of integers as input and returns the second-largest element in the list. If the 
list has fewer than two elements, the program should return None. For example, if the input list is [1, 2, 3, 2, 4, 5, 5], 
the program should return 5.
'''
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in lst:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i
    return second_largest
'''
Sort the following list by population. Calculate average and total population for cities from this list:
'''
cities = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942)
]

sorted_cities = sorted(cities, key=lambda x: x[1], reverse=True)

total_population = sum(city[1] for city in cities)
average_population = total_population / len(cities)

print("Sorted cities by population:")
for city in sorted_cities:
    print(city[0], city[1])
print("Total population:", total_population)
print("Average population:", average_population)
