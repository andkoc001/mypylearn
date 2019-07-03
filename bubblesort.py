# Andrzej Kocielski, 03-05-2019
# Bubblesort script
# ===


def bubblesort(lst):
    # definiuje zmienna 'passesLeft - od ostatniego elementu 'lst', w tyl do drugiego elementu
    for passesLeft in range(len(lst)-1, 0, -1):
        for index in range(passesLeft):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


l = [66, 89, 49, 62, 9, 53, 59]
print(l)
print(bubblesort(l))
