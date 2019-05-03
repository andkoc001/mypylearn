# Andrzej Kocielski, 03-05-2019
# Sequencing within list types
# ===

# for passesLeft in range(len(lst)-1, 0, -1):
lst = [66, 89, 49, 62, 9, 53, 59]
print(lst)  # ilosc uporzadkowane elementy obiektu 'lst'
print(len(lst))  # ilosc elementow obiektu 'lst'
print(lst[0])  # wartos pierwszego elementu obiektu 'lst'
print(lst[(len(lst)-1)])  # wartos ostatniego elementu obiektu 'lst'
print(lst[-1])  # to samo co powyzej
for i in (range(len(lst)-1, -1, -1)):  # zlicza od ostatniego elementu do pierwszego
    print(i, lst[i])
