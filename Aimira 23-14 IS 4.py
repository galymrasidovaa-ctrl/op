a10 = [12, 3, 5, 8, 7, 10, 11, 14, 9, 2]

odd_numbers = [x for x in a10 if x % 2 != 0]

if odd_numbers:
    max_odd = max(odd_numbers)
    print("Maks nechetnyh chisel net:", max_odd)
else:
    print("Massivte nechetnyh chisel net ")

A = [
    [1, 2, 3, 10],
    [5, 6, 20, 8],
    [9, 30, 11, 12],
    [40, 14, 15, 16]
]

n = 4

# Kosymsha diagonal element: A[i][n-1-i]
secondary_diagonal = [A[i][n - 1 - i] for i in range(n)]

max_secondary = max(secondary_diagonal)

print("Kosymsha diagonal elementtery:", secondary_diagonal)
print("Kosymsha diagonal boiynsha maks element:", max_secondary)
