# 2'. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) =
# ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

xp = [False, True]
yp = [False, True]
zp = [False, True]

if not (xp or yp or zp) == ((not xp) and (not yp) and (not zp)):
    print('True')
else:
    print('False')
