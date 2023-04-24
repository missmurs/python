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