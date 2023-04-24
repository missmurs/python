
'''
Write a game where user should guess of a capital of the country that you have in your dictionary.

capitals = { 'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'USA': 'Washington', 'Canada':
'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo',
'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia',
'Greece': 'Athens', ... }

You should show user a random country from the list and ask him to guess the capital. If user input right capital,
print "You are right!", add him a point and ask him to guess another country. If not, you should ask again. User should
be able to quit the game by typing "exit". You should print current score after each round. Also, you should print the
final score before user quit the game.

Give user a hint if he guesses wrong. Hint should looks like first letter of the capital. If you user make another mistake,
you should print one more letter from the capital.

If user make a mistake you should decrement his lives. Initial amount of lives is 3. Game will end when user has no
lives left. You should print the final score after user has no lives left.
'''
import random

capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}

lives = 3
score = 0

while lives > 0:
    country = random.choice(list(capitals.keys()))
    capital = capitals[country]
    guess = input(f"What is the capital of {country}? (type 'exit' to quit)").strip().capitalize()

    while guess != capital:
        if guess == 'Exit':
            break

        lives -= 1
        hint = capital[:len(capital) - (lives if lives < len(capital) else len(capital))]
        print(f"Wrong! Hint: {hint}")
        guess = input("Try again: ").strip().capitalize()

    if guess == 'Exit':
        break

    score += 1
    print("You are right!")
    print(f"Current score: {score}")
    print(f"Current lives: {lives}\n")

print(f"Final score: {score}")

'''
Optional Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
can be placed before D (500) and M (1000) to make 400 and 900.
'''

def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
    return result

'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than any other element. You may assume that the majority element always exists in the array.
'''
def majority_element(nums: list) -> int:
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return max(counts, key=counts.get)

def test_majority_element():
    result1 = majority_element([3, 2, 3])
    assert result1 == 3

    result2 = majority_element([2, 2, 1, 1, 1, 2, 2])
    assert result2 == 2

test_majority_element()

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"

Output: 3 Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"

Output: 1 Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def length_of_longest_substring(s: str) -> int:

    start, end = 0, 0
    longest_length = 0
    chars = set()

    while end < len(s):

        if s[end] not in chars:
            chars.add(s[end])
            end += 1
            longest_length = max(longest_length, end - start)

        else:
            chars.remove(s[start])
            start += 1

    return longest_length

'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
            return False
        if t[i] in t_to_s and t_to_s[t[i]] != s[i]:
            return False
        s_to_t[s[i]] = t[i]
        t_to_s[t[i]] = s[i]

    return True
