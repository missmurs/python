'''
Practice block 1:
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
'''


def outer_function(a, b):
    def inner_function():
        return a + b

    addition = inner_function()
    result = addition + 5
    return result
'''
Practice block 2
Write a program that asks user to enter an integer and convert it to int. If the user enters something that is not an 
integer, program should catch an error and ask the user to enter an integer again. if user inputs an integer, program 
should print this number and quit w/o any error.
'''
while True:
    try:
        num = int(input("Please enter an integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("That was not an integer. Please try again.")

'''
Write a program that asks the user to input a string and an integer n. Then display the character at index n in the 
string. You should handle an error properly and display proper error message.
'''
while True:
    try:
        string = input("Please enter a string: ")
        n = int(input("Please enter an integer index: "))
        char = string[n]
        print("The character at index {} in the string is: {}".format(n, char))
        break
    except IndexError:
        print("Index out of range. Please enter an integer within the range of the string.")
    except ValueError:
        print("Invalid index. Please enter an integer.")
'''
Practice block 3:
Write a function that simulate a dice roll and returns the result from 1 to 6.
'''
import random

def roll_dice():
    return random.randint(1, 6)

result = roll_dice()
print(result)
'''
Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
'''
import random

def dice_rolls():
    rolls = [0, 0, 0, 0, 0, 0]
    for i in range(10000):
        roll = random.randint(1, 6)
        rolls[roll-1] += 1
    return rolls
'''
Simulate an election for two candidates. Program should take amount of regions and rating for 1st candidate in each 
region (in percentage). Program should run election in every region. In every region, program should ask 10 000 voters. 
Candidate count as a winner if he gains more than 50% of all votes. Program should print the result of the election for 
each region and the winner
'''
import random

num_regions = int(input("Введіть кількість регіонів: "))

results = []

for i in range(num_regions):

    rating = random.randint(10, 100)

    rating /= 100

    votes_candidate_1 = 0
    votes_candidate_2 = 0
    for j in range(10000):

        if random.random() < rating:
            votes_candidate_1 += 1
        else:
            votes_candidate_2 += 1

    if votes_candidate_1 > votes_candidate_2:
        winner = "Перший кандидат"
    elif votes_candidate_2 > votes_candidate_1:
        winner = "Другий кандидат"
    else:
        winner = "Нічия"

    results.append((votes_candidate_1, votes_candidate_2, winner))

total_votes_candidate_1 = sum(r[0] for r in results)
total_votes_candidate_2 = sum(r[1] for r in results)

if total_votes_candidate_1 > total_votes_candidate_2:
    winner = "Перший кандидат"
elif total_votes_candidate_2 > total_votes_candidate_1:
    winner = "Другий кандидат"
else:
    winner = "Нічия"

print("\nРезультати виборів:")
print(f"Перший кандидат: {total_votes_candidate_1} голосів ({total_votes_candidate_1/num_regions/10000*100:.2f}% від загальної кількості голосів)")
print(f"Другий кандидат: {total_votes_candidate_2} голосів ({total_votes_candidate_2/num_regions/10000*100:.2f}% від загальної кількості голосів)")
print(f"Переміг {winner}")