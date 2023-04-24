'''
You have 100 cats.

One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). Write a program that simply outputs which cats have hats at the end.
'''

cats = [False] * 100
for i in range(1, 101):
    for j in range(i-1, 100, i):
        cats[j] = not cats[j] 
for i, has_hat in enumerate(cats):
    if has_hat:
        print("Cat", i+1, "has a hat!")

