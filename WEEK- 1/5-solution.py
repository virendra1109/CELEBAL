# Assignment iterables and iterators
from itertools import combinations

def probability_of_a(N, letters, K):
    indices = range(N)
    combs = list(combinations(indices, K))
    
    count_valid_combs = 0
    for comb in combs:
        if any(letters[i] == 'a' for i in comb):
            count_valid_combs += 1
            
    total_combs = len(combs)
    probability = count_valid_combs / total_combs
    
    return round(probability, 3)

N = int(input().strip())
letters = input().strip().split()
K = int(input().strip())
print(probability_of_a(N, letters, K)) 