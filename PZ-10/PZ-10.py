# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль.

# определяем товары в каждом магазине
magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}

# в каких магазинах нельзя приобрести сыр
stores_without_cheese = []
if 'сыр' not in magnit:
    stores_without_cheese.append('Магнит')
if 'сыр' not in pyaterochka:
    stores_without_cheese.append('Пятерочка')
if 'сыр' not in perekrestok:
    stores_without_cheese.append('Перекресток')

print("Магазины, в которых нельзя приобрести сыр:", stores_without_cheese)

# в каких магазинах можно приобрести одновременно молоко и сахар
stores_with_milk_and_sugar = []
if 'молоко' in magnit and 'сахар' in magnit:
    stores_with_milk_and_sugar.append('Магнит')
if 'молоко' in pyaterochka and 'сахар' in pyaterochka:
    stores_with_milk_and_sugar.append('Пятерочка')
if 'молоко' in perekrestok and 'сахар' in perekrestok:
    stores_with_milk_and_sugar.append('Перекресток')

print("Магазины, в которых можно приобрести одновременно молоко и сахар:", stores_with_milk_and_sugar)

# в каких магазинах можно приобрести соль
stores_with_salt = []
if 'соль' in magnit:
    stores_with_salt.append('Магнит')
if 'соль' in pyaterochka:
    stores_with_salt.append('Пятерочка')
if 'соль' in perekrestok:
    stores_with_salt.append('Перекресток')

print("Магазины, в которых можно приобрести соль:", stores_with_salt)
