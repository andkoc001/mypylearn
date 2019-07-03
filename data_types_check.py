# Andrzej Kocielski, 03-05-2019
# Testing data type (after division)
# ===

# Poniższa funkcja sprawdza jakiego typu jest przekazana wartość


def typing(x):
    if type(x) is int:
        return "Integer"

    if type(x) is float:
        return "Float"

    else:
        return "Unknown"


monthly_income = 3000
daily_income = monthly_income / 31
# pytanie czy daily_income jest integer czy float
print(typing(daily_income))

# print(daily_income)  # check
