import itertools

def permutations(n):
    lst = [i for i in range(1, n+1)]
    return list(itertools.permutations(lst))

perms = permutations(6)

print(len(perms))

for p in perms:
    temp = []
    for i in p:
        temp.append(str(i))
    print(" ".join(temp))