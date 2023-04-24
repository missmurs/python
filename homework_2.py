import random

num_regions = int(input("Введіть кількість регіонів: "))

results = []

for i in range(num_regions):

    rating = random.randint(10, 100)
    # переводимо відсотки у дробовий формат
    rating /= 100

    # запускаємо вибори в поточному регіоні
    votes_for_candidate_1 = 0
    votes_for_candidate_2 = 0
    for j in range(10000):
        # кожен виборець голосує випадковим чином
        if random.random() < rating:
            votes_for_candidate_1 += 1
        else:
            votes_for_candidate_2 += 1

    # визначаємо переможця виборів у поточному регіоні
    if votes_for_candidate_1 > votes_for_candidate_2:
        winner = "Перший кандидат"
    elif votes_for_candidate_2 > votes_for_candidate_1:
        winner = "Другий кандидат"
    else:
        winner = "Нічия"

    # зберігаємо результати виборів у поточному регіоні
    results.append((votes_for_candidate_1, votes_for_candidate_2, winner))

# підраховуємо загальний результат виборів
total_votes_for_candidate_1 = sum(r[0] for r in results)
total_votes_for_candidate_2 = sum(r[1] for r in results)

# визначаємо переможця загалом
if total_votes_for_candidate_1 > total_votes_for_candidate_2:
    winner = "Перший кандидат"
elif total_votes_for_candidate_2 > total_votes_for_candidate_1:
    winner = "Другий кандидат"
else:
    winner = "Нічия"